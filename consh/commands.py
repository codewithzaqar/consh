import subprocess
import os
from consh.utils import get_env_var

def execute_command(command, args):
    # Custom commands
    if command == "exit":
        exit(0)
    elif command == "hello":
        return f"Hello, {args[0] if args else 'User'}!"
    elif command == "env":
        key = args[0] if args else None
        return get_env_var(key)
    
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