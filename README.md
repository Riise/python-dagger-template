# Python (w/Dagger) Project Template

_For new projects clear this file and create a project specific README._

This is a template for a Python project using [Dagger.io](https://dagger.io/) as CI/CD engine. It is intended to be used as a starting point for creating a new project.

The project contains the following elements:

- VS Code workspace configuration (incl. recommended extensions).
- VS Code development container configuration.
- Pytest configuration.
- Code formatter, type checker, and linter configuration.
- Python code security scanner configuration ([Bandit](https://github.com/PyCQA/bandit) and [Pylint Secure Coding Standard](https://github.com/Takishima/pylint-secure-coding-standard)).
- Dependency vulnerability scanning ([Safety](https://safetycli.com/) or [pip-audit](https://pypi.org/project/pip-audit/)).
- Dagger CI pipeline running the above.
- GitHub workflows running the Dagger CI pipeline.

_Only one of the dependency vulnerability scanners is needed and the other can be removed._

To get started see [Development Environment Setup](./docs/dev-env-setup.md) and [Development Guide](./docs/DEVELOPMENT.md).

## Example CI

The GitHub workflows [`ci.yml`](./.github/workflows/ci.yml) and [`ci-2.yml`](./.github/workflows/ci-2.yml) are examples of how to run Dagger via GitHub and they both run the same CI pipeline. `ci-2.yml` has just split the pipeline into multiple GitHub jobs for better GitHub visualization, but takes longer to run as Dagger is initialized for every job.

The Dagger CLI can, apart from via GitHub, also be invoked locally from the host OS but not from inside the dev container. If Dagger CLI is not installed on the host OS and should be invoked inside the container then uncomment the specified lines in the [devcontainer.json](./.devcontainer/devcontainer.json) and the [devcontainer-setup.sh](./scripts/devcontainer-setup.sh) files.

_Note! Giving access to host Docker from the container has security implications._
