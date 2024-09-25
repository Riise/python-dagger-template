# Python Project Template

This is a template for a Python project. It is intended to be used as a starting point for creating a new project.

The project contains the following elements:

- VS Code workspace configuration (incl. recommended extensions).
- VS Code development container configuration.
- Pytest configuration.
- Code formatter, type checker, and linter configuration.
- Python security scanner configuration ([Bandit](https://github.com/PyCQA/bandit) and [Pylint Secure Coding Standard](https://github.com/Takishima/pylint-secure-coding-standard)).

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository.
2. Open the repository in VS Code.
3. Reopen the repository in the development container ([Windows](https://code.visualstudio.com/docs/devcontainers/containers#_open-a-wsl-2-folder-in-a-container-on-windows)).
    - The development container is configured to use Python 3.10 from a base Python image.
    - VS Code extensions defined in `.devcontainer/devcontainer.json` will be installed.
    - `requirements-dev.txt` (incl. `requirements.txt`) project dependencies will be installed.
4. Start coding!

## Project Structure

The project structure is as follows:

```bash
.
├── .vscode/                   # Shared VS Code workspace configuration
├── .devcontainer/             # Development container configuration
├── scripts/                   # CLI scripts
|   └── devcontainer-setup.sh  # Development container setup (ref. in devcontainer.json)
├── src/                       # Source code
├── tests/                     # Unit tests
├── docs/                      # Main documentation
├── .pylintrc                  # Pylint configuration
├── bandit.yaml                # Bandit configuration
├── requirements.txt           # Base pip installs (production only uses this)
├── requirements-dev.txt       # Development pip installs
├── requirements-ci.txt        # CI pip installs
└── ...
```
