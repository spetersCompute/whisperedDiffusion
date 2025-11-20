#!/bin/bash
if [ -z "$1" ]; then
  echo "Usage: ./run_cpu.sh input.wav [output.png]"
  exit 1
fi

INPUT="$1"
OUTPUT="${2:-output.png}"
HOST_BASE_PATH="/opt/container-data/whisper-app"

#Only keep the filename, no host path
BASENAME=$(basename "$INPUT")

#Require the file to EXIST inside ./input/
if [ ! -f "input/$BASENAME" ]; then
	echo "Error: File input/$BASENAME not found."
	echo "Put your audio file into the ./input/ directory first"
	exit 1
fi

#Use the full path for the audio file on the HOST machine
HOST_AUDIO_PATH="$(pwd)/input/$BASENAME"

podman run --rm \
  -v $HOST_BASE_PATH/input:/app/input:Z \
  -v $HOST_BASE_PATH/output:/app/output:Z \
  --user $(id -u):$(id -g) \
  whispered-diffusion:cpu \
  "/app/input/$BASENAME" --out-image "/app/output/$OUTPUT"
