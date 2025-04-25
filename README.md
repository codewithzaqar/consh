# Consh
A simple Python-based CLI insoired by xonsh

## Installation
```bash
pip install .
```

## Requirements
- Python 3.6+
- `prompt_toolkit>=3.0.0`

## Usage 
Run the CLI
```bash
consh
```
Available commands:
- `hello [name]`: Prints a greeting.
- `env [key]`: Shows environment variables.
- `version`: Displays the Consh version.
- `cd [path]`: Changes the current directory (defaults to home if no path).
- `alias [name='command']`: Sets or lists aliases (e.g., `alias ll='ls -l'`).
- `setenv key=value`: Sets an environment variable
- `help [command]`: Displays help for commands.
- `clear`: Clears the terminal screen.
- `source script.consh`: Executes a .consh script. 
- `exit`: Quits the CLI.
- System commands (e.g., Initialized empty Git repository in /home/user/consh/.git/is, pwd) with piping (e.g., ls | grep txt) and redirection (e.g., is > output.txt).
- Python expressions (e.g., `print(1+2)` or `x=5; print(x)`).