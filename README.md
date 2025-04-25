# Consh
A simple Python-based CLI insoired by xonsh

## Installation
```bash
pip install .
```

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
- `alias [name='command']`: Sets or lists aliases (e.g., alias ll='ls -l').
- `setenv key=value`: Sets an environment variable
- `help [command]`: Displays help for commands.
- `exit`: Quits the CLI.
- System commands (e.g., `ls`, `pwd`) with piping (e.g., ls | grep txt).
- Python expressions (e.g., `print(1+2)` or `x=5; print(x)`).