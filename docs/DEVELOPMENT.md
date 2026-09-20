# Development Guide

This document provides a reference for development practices and tools used in this project.

## Assumption & Pre-requisites

- The project is developed using Visual Studio Code and the development container.
- The development container is configured to use Python 3.14.
- Windows was used as the development environment, but development can happen on other operating systems.
- Linux was used as the development container.
- Production environment is assumed to be Linux-based.

### Windows Pre-requisites

For development on Windows, the following pre-requisites are required:

- [Windows Subsystem for Linux (WSL) 2](https://docs.microsoft.com/en-us/windows/wsl/install)
- [Docker Desktop](https://www.docker.com/products/docker-desktop) or [Rancher Desktop](https://rancherdesktop.io/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git for Windows](https://git-scm.com/download/win)
- [Dagger CLI](https://dagger.io/dagger-engine)

See local Windows installation guide here: [docs/dev-env-setup.md](./dev-env-setup.md).

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository.
2. Open the repository in VS Code.
3. Reopen the repository in the development container ([on Windows](https://code.visualstudio.com/docs/devcontainers/containers#_open-a-wsl-2-folder-in-a-container-on-windows)).
4. Start coding!

## Development Container

The project uses a development container to ensure a consistent development environment across all developers. The development container is defined in `.devcontainer/devcontainer.json` and uses the following configuration:

- It is from a Python 3.14 base image.
- Recommended VS Code extensions will be installed.
- Project dependencies are installed via [uv](https://docs.astral.sh/uv/) (`uv sync --group dev`).

## Project Structure

The project structure is as follows:

```bash
.
├── .vscode/                   # Shared VS Code workspace configuration
├── .devcontainer/             # Development container configuration
├── scripts/                   # CLI scripts
│   ├── ci-container-setup.sh  # Dagger CI container setup (ref. by Dagger)
│   └── devcontainer-setup.sh  # Development container setup (ref. in devcontainer.json)
├── src/                       # Source code
├── tests/                     # Unit tests
├── docs/                      # Main documentation
├── pyproject.toml             # Project metadata and dependency groups
├── uv.lock                    # Locked, reproducible dependency versions
└── ...
```

## Python Dependency Management

The project uses [uv](https://docs.astral.sh/uv/) for Python packaging and dependency management.

- `uv add <package>` adds a production dependency.
- `uv add --group ci <package>` adds a tool dependency needed to lint, scan, or test the code (used by both local dev and the Dagger CI container).
- `uv add --group dev <package>` adds a dependency needed only for local development (e.g. `dagger-io`, for IDE support while editing the Dagger module).
- `uv sync --group dev` refreshes your local environment with everything above (the `dev` group includes the `ci` group plus local-only extras).
- `uv run <command>` runs a command inside the project's managed environment.

The Dagger CI container installs only the `ci` group, via `uv sync --only-group ci` (plain `--group ci` isn't enough, since uv also syncs the `dev` default group unless told otherwise); it deliberately excludes `dagger-io` since the CI container doesn't need it.

## CI: Linting, Code Security Scanning, and Dependency Vulnerability Scanning

The project uses [Bandit](https://github.com/PyCQA/bandit) and [Pylint Secure Coding Standard](https://github.com/Takishima/pylint-secure-coding-standard) to scan for security vulnerabilities and code quality issues.

Both tools have VS Code extensions installed for real-time scanning, but they can also be run from the command line.

The project uses [pip-audit](https://pypi.org/project/pip-audit/) to scan for Python dependencies with known security vulnerabilities.

The configuration files are located in the root of the project:

- [`.pylintrc`](../.pylintrc): Pylint configuration.
- [`bandit.yml`](../bandit.yml): Bandit configuration.

### Running CI Locally

[Dagger.io](https://dagger.io/) is used as CI/CD engine and the CLI must be invoked from the host OS and not from within the development container.

If you already have created and configured a [Dagger Cloud](https://dagger.io/cloud) user you can log in from the current shell to log and view Dagger traces online.

```powershell
dagger login
```

To run the full CI locally run:

```powershell
dagger call ci --prj .
```

To run linting, code scanning, or tests:

```powershell
dagger call lint --prj .        # pylint + bandit
dagger call scan --prj .        # pip-audit
dagger call test --prj .        # pytest
```

To run individual CI steps run one of the following:

```powershell
dagger call pylint --prj .      # Code linting
dagger call bandit --prj .      # Code security scanning
dagger call pip-audit --prj .   # Dependency vulnerability scanning (pip-audit)
dagger call pytest --prj .      # Unit testing
```

### Running Linters and Scanners from the Command Line (outside Dagger)

To run Pylint with Secure Coding Standard:

```bash
pylint src
```

To run Bandit security scanner:

```bash
bandit -r src               # only source code folder
bandit -c bandit.yml -r .   # entire project and using a Bandit config file
```

To run pip-audit dependency vulnerability scanner:

```bash
pip-audit --path .venv
```

## The use of FIXME and TODO

The project uses the [TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight) extension to highlight `TODO`, and `FIXME` comments and a CI check should be setup to fail if any FIXMEs are present in a `main` branch merge request. Pylint checks for "fixme" comments.

The convention is to use `FIXME` for tasks that need to be fixed before the PR can be approved and merged. See it as notes to yourself about incomplete code or security issues that need to be addressed.

`TODO` is for tasks that need to be done sometime in the future. It can be used for improvements, refactoring, or other tasks that are not blocking the PR.

Note! It should be a comment line starting with TODO or FIXME followed by a colon and a space.

Example:
<pre># FIXME&colon; Add input validation.</pre>
