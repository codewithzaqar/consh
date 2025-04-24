import subprocess
import os
from consh.utils import get_env_var
from . import __version__

def get_available_commands():
    """Return list of available commands for tab completion."""
    return [
        "exit", "hello", "env", "version", "cd", "ls", "pwd", "cat",  # Common system commands
    ]

def execute_command(command, args):
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
        return f"Command failed: {e.stderr.strip()}"
    except FileNotFoundError:
        return f"Command '{command}' not found"