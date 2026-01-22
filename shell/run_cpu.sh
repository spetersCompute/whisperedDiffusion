#!/bin/bash

set -e

if [ -z "$1" ]; then
  echo "Usage: ./run_cpu.sh input.wav [output.png]"
  exit 1
fi

INPUT="$1"
OUTPUT="${2:-output.png}"

# Ensure host input/output dirs exist
mkdir -p input output

# Print diagnostic info
echo "[*] Using bind mounts:"
echo "    input  -> $(pwd)/input"
echo "    output -> $(pwd)/output"
echo

# Run inside container
podman run --rm \
  -v "$(pwd)/input:/app/input:Z" \
  -v "$(pwd)/output:/app/output:Z" \
  -v "$(pwd)/cache:/cache:Z" \
  -e HF_HOME=/cache \
  whispered-diffusion:cpu \
  "/app/input/$(basename "$INPUT")" --out-image "/app/output/$OUTPUT"
