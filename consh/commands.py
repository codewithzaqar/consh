import subprocess
import os
import ast
from consh.utils import get_env_var
from consh.config import get_aliases, set_alias
from . import __version__

def get_available_commands():
    """Return list of available commands for tab completion."""
    commands = [
        "exit", "hello", "env", "version", "cd", "alias", "ls", "pwd", "cat",  # Common system commands
    ]
    commands.extend(get_aliases().keys())  # Include aliases
    return commands

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