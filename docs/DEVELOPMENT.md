# Development Guide

This document provides a reference for development practices and tools used in this project.

## Assumption & Pre-requisites

- The project is developed using Visual Studio Code and the development container.
- The development container is configured to use Python 3.12.
- Windows was used as the development environment, but development can happen on other operating systems.
- Linux was used as the development container.
- Production environment is assumed to be Linux-based.

### Windows Pre-requisites

For development on Windows, the following pre-requisites are required:

- [Windows Subsystem for Linux (WSL) 2](https://docs.microsoft.com/en-us/windows/wsl/install)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git for Windows](https://git-scm.com/download/win)

See local Windows installation guide here: [docs/dev-env-setup.md](./dev-env-setup.md).

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository.
2. Open the repository in VS Code.
3. Reopen the repository in the development container ([on Windows](https://code.visualstudio.com/docs/devcontainers/containers#_open-a-wsl-2-folder-in-a-container-on-windows)).
4. Start coding!

## Development Container

The project uses a development container to ensure a consistent development environment across all developers. The development container is defined in `.devcontainer/devcontainer.json` and uses the following configuration:

- It is from a Python 3.12 base image.
- Recommended VS Code extensions will be installed.
- `requirements-dev.txt` (incl. `requirements.txt`) project dependencies will be installed.

## Project Structure

The project structure is as follows:

```bash
.
├── .vscode/                   # Shared VS Code workspace configuration
├── .devcontainer/             # Development container configuration
├── scripts/                   # CLI scripts
│   └── devcontainer-setup.sh  # Development container setup (ref. in devcontainer.json)
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

## Python Dependency Management

Add application/production dependencies to `requirements.txt` and development tool dependencies to `requirements-dev.txt`. If you need to install additional dependencies for CI, add them to `requirements-ci.txt`.

## Linting and Security Scanning

The project uses [Bandit](https://github.com/PyCQA/bandit) and [Pylint Secure Coding Standard](https://github.com/Takishima/pylint-secure-coding-standard) to scan for security vulnerabilities and code quality issues. The configuration files are located in the root of the project:

- [`.pylintrc`](../.pylintrc): Pylint configuration.
- [`bandit.yaml`](../bandit.yaml): Bandit configuration.

To run the Pylint linting and security scan, use the following command:

```bash
pylint ./src/
```

To run the Bandit security scan, use the following command:

```bash
bandit -r ./src/                 # only the source code 
bandit -c ./bandit.yaml -r .     # the entire project and using the Bandit config file
```
