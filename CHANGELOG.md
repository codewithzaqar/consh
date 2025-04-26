# Changelog

All notable changes to the Consh project will be documented in this file.

## [0.07] - 2025-04-26

### Added
- `CODE_OF_CONDUCT.md` using Contributor Covenant v2.1 to foster a welcoming community.
- `CONTRIBUTING.md` with guidelines for reporting issues, proposing features, and submitting pull requests.
- GitHub issue templates (`bug_report.md`, `feature_request.md`, `config.yml`) to streamline issue reporting.
- `CHANGELOG.md` to document project changes.

### Fixed
- `config.py`: Added `None` check for alias and environment variable values to prevent `AttributeError` during `conshrc` parsing.

### Changed
- Updated `README.md` with repository description, contributing, issue reporting, and changelog sections.
- Updated `.gitignore` to include `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, and `.github/`.
- Incremented version to `0.07` in `setup.py`.

## [0.06] - 2025-04-25
- Added append redirection (`>>`) for output files.
- Implemented job control with `bg` and `fg` commands.
- Added customizable prompt via `conshrc` `[prompt]` section.
- Enabled command logging to `.consh_log` for debugging.
- Improved error handling in `config.py` for `conshrc` parsing.

## [0.05] - 2025-04-24
- Added output redirection (`>`) for commands.
- Implemented script execution with `source` command for `.consh` files.
- Added `clear` command to clear the terminal screen.
- Enhanced tab completion for file paths and commands.

## [0.04] - 2025-04-23
- Added piping support for commands (e.g., `ls | grep txt`).
- Implemented `setenv` command for environment variables.
- Added help system with `help [command]`.
- Supported environment variables in `conshrc`.

## [0.03] - 2025-04-22
- Added Python expression execution (e.g., `print(1+2)`).
- Implemented `alias` command for alias management.
- Added `conshrc` configuration for aliases and settings.
- Improved error handling for invalid commands.

## [0.02] - 2025-04-21
- Added tab completion for commands and aliases.
- Implemented command history saved to `.consh_history`.
- Added `cd` and `version` commands.

## [0.01] - 2025-04-20  
- Initial release with basic shell functionality.
- Supported system commands (e.g., `ls`, `pwd`).
- Basic Python-based CLI structure inspired by xonsh.