#!/bin/bash

# PIP install packages
if [ -f "requirements-ci.txt" ]; then
    pip install -r requirements-ci.txt
fi

echo "ci-container-setup.sh complete."
