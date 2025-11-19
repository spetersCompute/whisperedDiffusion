# WhisperedDiffusion: Audio-to-Image Pipeline (Whisper + Stable Diffusion)

**Speech → Text → Image generation pipeline**  
Powered by **Faster-Whisper** + **Stable Diffusion Turbo**.  
Runs locally on **CPU** or **NVIDIA GPUs** using Podman or Docker.

---

## What It Does

1. Takes an **audio file** as input
2. Transcribes it to text using **Faster-Whisper**
3. Feeds the transcript into **Stable Diffusion**
4. Outputs an image — fully **offline**, no APIs or cloud

---

## Quick Start (CPU)

```bash
podman build -f Dockerfile.cpu -t whispered-diffusion:cpu .
./run_cpu.sh input/audio.wav
```

Output will appear in: `output/`

---

## Quick Start (NVIDIA GPU)

**Requires:**
* Nvidia GTX 10 series, RTX 20 series and up 
- Nvidia drivers
- Nvidia container toolkit

### Build the container:
```bash
podman build -f Dockerfile.nvidia -t whispered-diffusion:nvidia .
```

### Run:
```bash
./run_nvidia.sh input/audio.wav
```

---

## Project Structure

```
whisperedDiffusion/
├─ Dockerfile.cpu
├─ Dockerfile.nvidia
├─ run_cpu.sh
├─ run_nvidia.sh
├─ requirements.txt
├─ src/
│  ├─ whisper_client.py
│  ├─ diffusion_client.py
│  └─ pipeline.py
├─ input/
└─ output/
```

---

## Requirements

- Podman **or** Docker
- No Python needed on host
- Optional: NVIDIA GPU + drivers

---

## Models Used

- Whisper via `faster_whisper`
- Stable Diffusion Turbo (`stabilityai/sd-turbo`)

Models download automatically inside the container.

---

## Why This Exists

Built to:
- Demo an end-to-end local AI pipeline
- Avoid cloud/SaaS dependency
- Serve as a real portfolio piece

**Version 1 is meant to be simple and reliable.**

---

## Roadmap

- SDXL or Flux support
- Prompt UI
- Live mic transcription
- Audio/video output

---

## License

MIT

---

## Notes

This is early-stage, but it **works**.  
Clone. Build. Run. Get an image.

---