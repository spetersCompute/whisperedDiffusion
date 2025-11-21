# Whispered Diffusion

**Speech → Text → Image**  
Whisper transcription + Stable Diffusion image generation  
Runs fully **locally** using **Python** — no APIs, no cloud, no accounts.

This project is built as a demonstration of an **end-to-end AI pipeline**, suitable for Upwork portfolio work.

---

## What It Does

1. Takes an audio file (spoken prompt)  
2. Transcribes it using **Faster-Whisper**  
3. Converts the transcript into an image prompt  
4. Generates an image using **Stable Diffusion Turbo**  
5. Saves the final output to disk

Everything runs on **CPU** by default.

---

# Bare-Metal Quick Start (No Docker)

### 1. Clone the project
```bash
git clone https://github.com/yourname/whisperedDiffusion.git
cd whisperedDiffusion
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
pip install torch==2.3.0
```

### 3. Run the pipeline
Put an audio file into the `input/` directory, then run:

```bash
python -m src.pipeline input/yourfile.wav --out-image output.png
```

Image appears in `output/`.

---

# Example Output

**Input Audio → Image Prompt → Final Image**

(Add samples later.)

---

# Project Structure

```
whisperedDiffusion/
├─ src/
│  ├─ pipeline.py
│  ├─ whisper_client.py
│  ├─ diffusion_client.py
│
├─ input/
├─ output/
├─ requirements.txt
└─ README.md
```

---

# Tech Used

### Whisper (via Faster-Whisper)
- Fast, accurate transcription  
- CPU-friendly  

### Stable Diffusion Turbo (`stabilityai/sd-turbo`)
- Fast text-to-image  
- Works without GPU

---

# Why This Exists

This project demonstrates:

✔ Building an AI pipeline from scratch  
✔ Running speech → text → image locally  
✔ Clean, documented code  
✔ Reproducible environments  

Perfect as an Upwork portfolio piece showcasing **real applied AI work**, not toy examples.

---

# Roadmap

- Intel Arc / OpenVINO acceleration  
- NVIDIA GPU container (CUDA)  
- Microphone live-transcription mode  
- More advanced diffusion models (SDXL, Flux)

---

# License

MIT