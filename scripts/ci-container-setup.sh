#!/bin/bash
set -euo pipefail

# uv is already copied into the container by ci_container() (see dagger_main.py).
# Create the project's uv-managed virtual environment and install CI dependencies only
# (--only-group is required since uv otherwise also syncs the "dev" default group)
uv sync --only-group ci

echo "ci-container-setup.sh complete."
