#!/bin/bash

ISSM_DIR="$(pwd)"
export ISSM_DIR

source .venv/bin/activate

mkdir -p build
if ! (
  cd build || exit

    if ! cmake -GNinja ..; then
      echo >&2 "Configuration failed"
      exit 1
    fi

  if ! cmake --build . -j; then
    echo >&2 "Build failed"
    exit 1
  fi
); then
  exit 1
fi

source etc/environment.sh

if ! python ./issm_newton.py; then
  echo >&2 "Experiment failed"
  exit 1
fi
