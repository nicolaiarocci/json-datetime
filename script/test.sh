#!/usr/bin/env bash
set -euvo pipefail
IFS=$'\n\t'

has() {
    type "$1" >/dev/null 2>&1
}

# stop the build if there are Python syntax errors or undefined names
flake8 jsondatetime --count --select=E9,F63,F7,F82 --show-source --statistics
# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
flake8 jsondatetime --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
# Ensure style conformity
has black && black --check jsondatetime
# Make sure it passes its tests
pytest
