#!/bin/bash

ISSM_DIR="$(pwd)"
export ISSM_DIR

source .venv/bin/activate

source etc/environment.sh

if ! python ./issm_newton.py; then
  echo >&2 "Experiment failed"
  exit 1
fi
