#!/bin/bash
if [ -z "$1" ]; then
  echo "Usage: ./run_cpu.sh input.wav [output.png]"
  exit 1
fi

INPUT="$1"
OUTPUT="${2:-output.png}"

podman run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  whispered-diffusion:cpu \
  "/app/input/$INPUT" --out-image "/app/output/$OUTPUT"