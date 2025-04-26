# Consh
Consh is a Python-based command-line interface (CLI) inspired by xonsh, blending traditional shell functionality with Python scripting. It offers features like piping, redirections, job control, customizable prompts, and script execution for a powerful and flexible user experience

## Code of Conduct
We are committed to fostering a welcoming and inclusive community. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) to understand the expctations for participation in the Consh project.

## Contributing
We welcome contributions to Consh! To get started, please read our [Contributing Guidelines](CONTRIBUTING.md) for details on submitting issues, proposing features, and creating pull requests.

## Reporting Issues
Found a bug or have a feature idea? Please use our [GitHub Issues](https://github.com/codewithzaqar/consh/issues) page and select the appropriate issue template (Bug Report or Feature Request) to provide detailed information. See the [Contributing Guidelines](CONTRIBUTING.md) for more details.

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
- `bg command [args]`: Runs a command in the foreground
- `fg [job_id]`: Brings a background job to the foreground.
- `exit`: Quits the CLI.
- System commands (e.g., Initialized empty Git repository in /home/user/consh/.git/is, pwd) with piping (e.g., ls | grep txt) and redirection (e.g., is > output.txt).
- Python expressions (e.g., `print(1+2)` or `x=5; print(x)`).