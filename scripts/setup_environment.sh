#!/usr/bin/env bash
set -euo pipefail

VENV_DIR="${1:-py3env}"

if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment '$VENV_DIR' already exists. To recreate, remove it first."
    exit 0
fi

python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"
pip install --upgrade pip
pip install biopython pandas
echo "Environment ready: source $VENV_DIR/bin/activate"
