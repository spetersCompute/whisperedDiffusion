# Whispered Diffusion

**Speech → Text → Image**  
A fully local voice-to-image AI pipeline using **Faster-Whisper** and **Stable Diffusion**.  
Runs on your machine, **no APIs, no cloud, no accounts**.

Built as a practical end-to-end AI systems project and portfolio demo.

---

## What It Does

1. Records a spoken prompt ('push-to-talk' via microphone)  
2. Transcribes speech using **Faster-Whisper**  
3. Converts transcript into an image prompt  
4. Generates an image using **Stable Diffusion Turbo**  
5. Saves the final output locally  

Everything runs **locally on CPU by default**.

---

## Quick Start (Bare Metal, No Docker)

### 1. Clone the project
```bash
git clone https://github.com/spetersCompute/whisperedDiffusion.git
cd whisperedDiffusion
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
pip install torch==2.3.0
```

### 3. Run the app
```bash
python -m src.app
```

### Controls
- Press `r` to start recording  
- Speak your prompt  
- Press `s` to stop recording  
- Image is generated automatically into `data/output/`

---

## Project Structure

```
whisperedDiffusion/
├─ src/
│  ├─ app.py            # Entry point / orchestration
│  ├─ capture.py        # Microphone + audio capture
│  ├─ pipeline.py       # Transcript → prompt → image
│  ├─ whisper_client.py
│  ├─ diffusion_client.py
│
├─ data/
│  ├─ input/            # Temporary audio files
│  ├─ output/           # Generated images
│  └─ cache/            # HuggingFace cache
├─ requirements.txt
└─ README.md
```

---

## Tech Used

- Python  
- Faster-Whisper (speech → text)  
- Stable Diffusion Turbo (text → image)  
- sounddevice (audio capture)  
- threading + callbacks  
- HuggingFace models (local inference)

---

## Why This Exists

This project demonstrates:

✔ Building a real end-to-end AI pipeline  
✔ Audio capture, threading, and real IO  
✔ Modular architecture (capture → app → pipeline)  
✔ Running AI systems locally instead of via cloud APIs   

---

## Roadmap

- Direct NumPy audio → Whisper (no temp WAV)  
- Streaming transcription mode  
- GPU acceleration (CUDA, OpenVINO, Intel Arc)  
- Containerized deployment (💀) 
- More advanced diffusion models (SDXL, Flux)

---

## License

MIT
