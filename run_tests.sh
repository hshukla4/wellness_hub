#!/bin/bash

# Set project root to the current directory
export PYTHONPATH=$(pwd)

# Run pytest with all standard options + any args you pass
pytest -s --disable-warnings "$@"
