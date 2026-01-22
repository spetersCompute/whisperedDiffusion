#!/bin/bash

# Whispered Diffusion — Bare-Metal CPU Launcher
# (ideal baseline before Udica / SELinux container policy)

set -e

if [ -z "$1" ]; then
  echo "Usage: ./run_local_cpu.sh input.wav [output.png]"
  exit 1
fi

INPUT="$1"
OUTPUT="${2:-output.png}"

# We use ONE directory for input/output/cache so the later container
# has exactly 1 mount point Udica can safely generate policy for.
DATADIR="./data"

mkdir -p "$DATADIR/input" "$DATADIR/output" "$DATADIR/cache"

# Strip to filename
BASENAME=$(basename "$INPUT")

# Copy input → data/input/
if [ ! -f "$DATADIR/input/$BASENAME" ]; then
  echo "[*] Copying $INPUT → $DATADIR/input/$BASENAME"
  cp "$INPUT" "$DATADIR/input/$BASENAME"
fi

echo "[*] Running pipeline…"

HF_HOME="$DATADIR/cache" \
python3 -m src.pipeline \
  "$DATADIR/input/$BASENAME" \
  --out-image "$DATADIR/output/$OUTPUT"

echo "[✓] Done — output saved to $DATADIR/output/$OUTPUT"
