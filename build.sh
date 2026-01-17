#!/bin/bash

ISSM_DIR="$(pwd)"
export ISSM_DIR

source .venv/bin/activate

mkdir -p build
if ! (
  cd build || exit

    if ! cmake -GNinja .. --fresh; then
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
