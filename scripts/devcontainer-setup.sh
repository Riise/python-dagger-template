#!/bin/bash
set -euo pipefail

# Install uv (Python package/dependency manager) if not already present
if ! command -v uv >/dev/null 2>&1; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# The installer places uv/uvx in $HOME/.local/bin; make sure this shell can see it
export PATH="$HOME/.local/bin:$PATH"

# Create/refresh the project's uv-managed virtual environment and install dev dependencies
uv sync --group dev

# Set the workspace directory as a Git safe directory
git config --global --add safe.directory /workspaces/python-dagger-template

echo "devcontainer-setup.sh complete."
