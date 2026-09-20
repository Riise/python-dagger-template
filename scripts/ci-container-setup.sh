#!/bin/bash

# Install uv (Python package/dependency manager)
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

# Create the project's uv-managed virtual environment and install CI dependencies only
# (--only-group is required since uv otherwise also syncs the "dev" default group)
uv sync --only-group ci

echo "ci-container-setup.sh complete."
