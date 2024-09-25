#!/bin/bash

# Upgrade pip
python -m pip install --upgrade pip

# Safety check upgrades (aparrently installed on base image)
pip install --upgrade setuptools
pip install --upgrade jinja2

# pip install packages
if [ -f "requirements-ci.txt" ]; then
    pip install -r requirements-ci.txt
fi

echo "ci-container-setup.sh complete."
