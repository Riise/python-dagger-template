# Development Reference

This document provides a reference for development practices and tools used in this project.

## Assumption & Pre-requisites

The project is developed using Visual Studio Code and the development container. The development container is configured to use Python 3.10. Windows was used to develop the project, but the project should work on other operating systems.

### Windows Pre-requisites

For development on Windows, the following pre-requisites are required:

- [Windows Subsystem for Linux (WSL) 2](https://docs.microsoft.com/en-us/windows/wsl/install)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git for Windows](https://git-scm.com/download/win)

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository.
2. Open the repository in VS Code.
3. Reopen the repository in the development container ([Windows](https://code.visualstudio.com/docs/devcontainers/containers#_open-a-wsl-2-folder-in-a-container-on-windows)).
    - `requirements-dev.txt` (incl. `requirements.txt`) project dependencies will automatically be installed.
4. Start coding!

## Python Dependency Management

Add application/production dependencies to `requirements.txt` and development tool dependencies to `requirements-dev.txt`. If you need to install additional dependencies for CI, add them to `requirements-ci.txt`.

## Python Security Scanning

The project uses [Bandit](https://github.com/PyCQA/bandit) and [Pylint Secure Coding Standard](https://github.com/Takishima/pylint-secure-coding-standard) to scan for security vulnerabilities and code quality issues. The configuration files are located in the root of the project:

- [`.pylintrc`](../.pylintrc): Pylint configuration.
- [`bandit.yaml`](../bandit.yaml): Bandit configuration.
