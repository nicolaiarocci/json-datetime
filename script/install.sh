#!/usr/bin/env bash
set -euvo pipefail
IFS=$'\n\t'

python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
