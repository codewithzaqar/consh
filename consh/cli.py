import sys
from .Parser import parse_command
from consh.commands import execute_command

def run_cli():
    print("Consh v0.01 - Type 'exit' to quit")
    while True:
        try:
            user_input = input("consh> ").strip()
            if not user_input:
                continue
            command, args = parse_command(user_input)
            result = execute_command(command, args)
            if result is not None:
                print(result)
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit")
        except Exception as e:
            print(f"Error: {e}")

def main():
    if len(sys.argv) > 1:
        # Handle direct command-line arguments (e.g., `consh ls`)
        command, args = parse_command(" ".join(sys.argv[1:]))
        result = execute_command(command, args)
        if result:
            print(result)
    else:
        run_cli()

if __name__ == "__main" or sys.argv[0] == "-c":
    main()