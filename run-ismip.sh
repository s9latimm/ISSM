#!/bin/bash

ISSM_DIR="$(pwd)"
export ISSM_DIR

source .venv/bin/activate

source etc/environment.sh

#(
#  cd examples/ISMIP/Models || exit
#  rm -vf ISMIP-Mesh_generation.nc
#  rm -vf ISMIP-SetMask.nc
#  rm -vf ISMIP-Parameterization.nc
#  rm -vf ISMIP-Extrusion.nc
#  rm -vf ISMIP-SetFlow.nc
#  rm -vf ISMIP-BoundaryCondition.nc
#  rm -vf ISMIP-StressBalance.nc
#)

mkdir -p build
if ! (
  cd build || exit

  if ! cmake --build . -j; then
    echo >&2 "Build failed"
    exit 1
  fi
); then
  exit 1
fi

if ! python ./issm_ismip.py; then
  echo >&2 "Experiment failed"
  exit 1
fi
