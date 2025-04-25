import subprocess
import os
import ast
import shutil
from consh.utils import get_env_var
from consh.config import get_aliases, set_alias
from consh.Parser import parse_pipeline
from . import __version__

def get_available_commands():
    """Return list of available commands for tab completion."""
    commands = [
        "exit", "hello", "env", "version", "cd", "alias", "setenv", "help", "clear", "source", "ls", "pwd", "cat", "grep"  # Common system commands
    ]
    commands.extend(get_aliases().keys())  # Include aliases
    return commands

def get_command_help():
    """Return help text for commands."""
    return {
        "exit": "Quits the Consh CLI.",
        "hello": "Prints a greeting. Usage: hello [name]",
        "env": "Shows environment variables. Usage: env [key]",
        "version": "Displays the Consh versions.",
        "cd": "Changes the current directory. Usage: cd [path]",
        "alias": "Sets or lists aliases. Usage: alias [name='command']",
        "setenv": "Sets an environment variable. Usage: setenv key=value",
        "help": "Displays help for commands. Usage: help [commands]",
        "clear": "Clears the terminal screen.",
        "source": "Executes a .consh script. Usage: source script.consh"
    }

def execute_pipeline(pipeline):
    """Execute a pipeline of commands with optional redirection."""
    if not pipeline:
        return None
    
    # Handle redirection
    output_file = None
    if pipeline and pipeline[-1][0] == ">":
        if len(pipeline[-1][1]) != 1:
            return "Usage: command > filename"
        output_file = pipeline[-1][1][0]
        pipeline = pipeline[:-1]
    
    # Single command case
    if len(pipeline) == 1:
        command, args = pipeline[0]
        result = execute_command(command, args)
        if output_file and result is not None:
            try:
                with open(output_file, "w") as f:
                    f.write(str(result))
                return None
            except Exception as e:
                return f"Redirection error: {e}"
        return result
    
    # Piping case
    processes = []
    for i, (command, args) in enumerate(pipeline):
        try:
            stdin = processes[-1].stdout if processes else None
            stdout = subprocess.PIPE if i < len(pipeline) - 1 else (open(output_file, "w") if output_file else None)
            process = subprocess.Popen(
                [command] + args,
                stdin=stdin,
                stdout=stdout,
                stderr=subprocess.PIPE,
                text=True
            )
            processes.append(process)
        except FileNotFoundError:
            return f"Command '{command}' not found"
        
    # Close intermediate pipes
    for p in processes[:-1]:
        p.stdout.close()

    # Get output and errors
    try:
        stdout, stderr = processes[-1].communicate()
        if processes[-1].returncode != 0:
            return f"Command failed: {stderr.strip() or 'Unknown error'} (exit code: {processes[-1].returncode})"
        return stdout.strip() if not output_file else None
    except Exception as e:
        return f"Pipeline error: {e}"
    finally:
        for p in processes:
            p.terminate()
        if output_file and processes[-1].stdout:
            processes[-1].stdout.close()

def execute_command(command, args):
    # Check for aliases
    aliases = get_aliases()
    if command in aliases:
        command, args = parse_alias_command(aliases[command], args)

    # Custom commands
    if command == "exit":
        exit(0)
    elif command == "hello":
        return f"Hello, {args[0] if args else 'User'}!"
    elif command == "env":
        key = args[0] if args else None
        return get_env_var(key)
    elif command == "version":
        return f"Consh v{__version__}"
    elif command == "cd":
        try:
            path = args[0] if args else os.path.expanduser("~")
            os.chdir(path)
            return f"Changed directory to {os.getcwd()}"
        except FileNotFoundError:
            return f"Directory not found: {args[0]}"
        except Exception as e:
            return f"Error changing directory: {e}"
    elif command == "alias":
        if not args:
            return "\n".join(f"{k}='{v}'" for k, v in aliases.items())
        if len(args) < 2 or args[0] != "=":
            return "Usage: alias name='command'"
        name, value = args[1].split("=", 1)
        set_alias(name, value.strip("'"))
        return f"Alias '{name}' set to '{value}'"
    elif command == "setenv":
        if not args or "=" not in args[0]:
            return "Usage: setenv key=value"
        key, value = args[0].split("=", 1)
        os.environ[key] = value
        return f"Set {key}={value}"
    elif command == "help":
        help_texts = get_command_help()
        if not args:
            return "\n".join(f"{cmd}: {desc}" for cmd, desc in help_texts.items())
        cmd = args[0]
        return help_texts.get(cmd, f"No help available for '{cmd}'")
    elif command == "clear":
        os.system("cls" if os.name == "nt" else "clear")
        return None
    elif command == "source":
        if not args:
            return "Usage: source script.consh"
        script_path = args[0]
        if not os.path.exists(script_path):
            return f"Script not found: {script_path}"
        if not script_path.endswith(".consh"):
            return "Script must have .consh extension"
        try:
            with open(script_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        pipeline = parse_pipeline(line)
                        result = execute_pipeline(pipeline)
                        if result:
                            print(result)
            return None
        except Exception as e:
            return f"Script execution error: {e}"
    
    # Try Python code execution
    try:
        result = try_python_exec(" ".join([command] + args))
        if result is not None:
            return str(result)
    except (SyntaxError, ValueError, NameError):
        pass
    
    # System commands
    try:
        result = subprocess.run(
            [command] + args,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Command failed: {e.stderr.strip() or 'Unknown error'} (exit code: {e.returncode})"
    except FileNotFoundError:
        return f"Command '{command}' not found"
    except Exception as e:
        return f"System command error: {e}"
    
def parse_alias_command(alias_value, args):
    """Parse alias value and combine with args."""
    parts = alias_value.strip().split()
    return parts[0], parts[1:] + args

def try_python_exec(code):
    """Attempt to execute code as Python expression or statement."""
    try:
        # Try as expression first
        tree = ast.parse(code, mode="eval")
        return eval(compile(tree, "<string>", "eval"))
    except SyntaxError:
        # Try as statement
        tree = ast.parse(code, mode="exec")
        exec(compile(tree, "<string>", "exec"))
        return None