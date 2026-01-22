#!/bin/bash
if [ -z "$1" ]; then
  echo "Usage: ./run_nvidia.sh input.wav [output.png]"
  exit 1
fi

INPUT="$1"
OUTPUT="${2:-output.png}"

podman run --rm --hooks-dir=/usr/share/containers/oci/hooks.d \
  --security-opt=no-new-privileges \
  --device nvidia.com/gpu=all \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  whispered-diffusion:nvidia \
  "/app/input/$INPUT" --out-image "/app/output/$OUTPUT"
