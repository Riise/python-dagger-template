#!/bin/bash

# PIP install packages
if [ -f "requirements-dev.txt" ]; then
    pip install -r requirements-dev.txt
fi

# Set the workspace directory as a Git safe directory
git config --global --add safe.directory /workspaces/python-template

echo "devcontainer-setup.sh complete."
