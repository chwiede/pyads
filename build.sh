#!/usr/bin/env bash

set -e

if [ -d dist ]; then
    rm -rf dist
fi

python setup.py sdist
python setup.py bdist_wheel