import sys
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter
from .Parser import parse_command
from consh.commands import execute_command, get_available_commands
from consh.config import load_config

def run_cli():
    # Load configuration (e.g., aliases)
    load_config() 

    # Initialize prompt with history and tab completion
    history = FileHistory(".consh_history")
    commands = get_available_commands()
    completer = WordCompleter(commands, ignore_case=True)
    session = PromptSession(
        "consh> ",
        completer=completer,
        history=history,
        complete_while_typing=True
    )

    print("Consh v0.03 - Type 'exit' to quit")
    while True:
        try:
            user_input = session.prompt().strip()
            if not user_input:
                continue
            command, args = parse_command(user_input)
            result = execute_command(command, args)
            if result is not None:
                print(result)
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit")
        except EOFError:
            break
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

if __name__ == "__main__" or sys.argv[0] == "-c":
    main()