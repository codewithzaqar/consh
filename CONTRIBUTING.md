# Contributing to Consh

Thank you for your interest in contributing to Consh! We welcome contributions from the community to make this Python-based CLI, inspired by xonsh, even better. This document outlines how to contribute effectively.

## Code of Conduct
All contributors are expected to adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it to understand the expectations for respectful and inclusive behavior.

## How to Contribute

### Reporting Issues
- Check the [GitHub Issues](https://github.com/codewithzaqar/consh/issues) page to ensure the issue hasn’t been reported.
- Open a new issue with a clear title and description, including:
  - Steps to reproduce the issue
  - Expected and actual behavior
  - Environment details (e.g., Python version, OS)
- Use labels (e.g., `bug`, `enhancement`) to categorize the issue.

### Suggesting Enhancements
- Propose new features via GitHub Issues with the `enhancement` label.
- Describe the feature, its use case, and potential implementation ideas.
- Engage in discussions to refine the proposal before submitting a pull request.

### Submitting Pull Requests
1. **Fork the Repository**:
   - Fork `https://github.com/codewithzaqar/consh` and clone your fork:
     ```bash
     git clone https://github.com/codewithzaqar/consh.git
     cd consh
     ```
2. **Set Up the Development Environment**:
   - Install dependencies:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     pip install -r requirements.txt
     pip install -e .
     ```
   - Verify the setup by running:
     ```bash
     consh
     ```
3. **Create a Branch**:
   - Create a branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make Changes**
   - Follow the project's coding style (PEP 8).
   - Add or update tests in a `tests/` directory (if applicable).
   - Update documentation (e.g., `README.md`, command help in `command.py`).
   - Ensure your changes don't break existing functionality.
5. **Test Your Changes**:
   - Run the CLI to verify functionality:
   ```bash
   consh
   ```
   - Test new commands or features (e.g., `your-new-command`).
6. **Commit Your Changes**:
   - Write clear commit messages:
   ```bash
   git commit -m "Add feature: your-feature-name with description"
   ```
7. **Push and Create a Pull Request**:
   - Push your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
   - Open a pull request on GitHub, referencing the related issue (e.g., `Fixes #123`).
   - Describe the changes, their purpose, and any testing done.
8. **Code Review**:
   - Respond to feedback from maintainers.
   - Make requested changes and push updates to the same branch.
   - Ensure the pull request passes any automated checks (if set up).

### Development Guidelines
- **Code Style**: Adhere to PEP 8. Use tools like `flake8` for linting.
- **Testing**: Add tests for new features or bug fixes (future `tests/` directory).
- **Documentation**: Update `README.md`, `CONTRIBUTING.md` or command help in `commands.py` as needed.
- **Commit Messages**: Use descriptive messages (e.g., `Fix bug in Parser.py for redirction`).
- **Scope**: Keep pull requests focused on a single feature or fix.

### Getting Help
- For questions, open a GitHub Issu with the `question` label.
- Contact maintainers via [consh-maintainers@example.com] for sensitive matters.
- Join discussions in GitHub Issues or Pull Requests to collaborate.

## License
By contributing, you agree that your contributions will be licensed under the MIT License, as the repository.

Thank you for helping make Consh better!