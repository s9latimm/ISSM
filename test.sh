#!/bin/bash

mkdir -p build
cd  build
cmake -GNinja .. --fresh && cmake --build . -j
if [ $? -ne 0 ]; then
    exit $?
fi
cd ..

export export ISSM_DIR=$(pwd)

source .venv/bin/activate
source etc/environment.sh

python ./issm_newton.py
if [ $? -ne 0 ]; then
    exit $?
fi
