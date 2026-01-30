import os
from pathlib import Path
import threading
import sounddevice as sd
import soundfile as sf
from src.whisper_client import WhisperClient

from src.pipeline import run_pipeline
from src.capture import recordPrompt, keyListener,callback, SAMPLE_RATE

def main():
    dataDir = Path("./data")
    (dataDir / "input").mkdir(parents=True, exist_ok=True)
    (dataDir / "cache").mkdir(parents=True, exist_ok=True)
    (dataDir / "output").mkdir(parents=True, exist_ok=True)

    os.environ["HF_HOME"] = str(dataDir / "cache")

    print("[App] Runtime initialized.")
    print("[App] HF cache:", dataDir / "cache")
    print("[App] Output dir:", dataDir / "output")

    print("""
    Welcome to whisperedDiffusion.

    A styling prefix is applied:
    'A vibrant neon synthwave 
     illustration of a... (your prompt)"
     
    Press 'r' to record your prompt
    Press 's' to stop recording



    """)

    t = threading.Thread(target=keyListener, daemon=True)
    t.start()
    with sd.InputStream(callback=callback, channels=1, samplerate=SAMPLE_RATE):
        audio, samplerate = recordPrompt()
        sf.write(dataDir / "input" / "prompt.wav", audio, samplerate)

    whisper = WhisperClient(
        model_name="base.en",
        device="cpu",
        compute_type="int8"
    )

    wav_path = str(dataDir / "input" / "prompt.wav")
    transcript = whisper.transcribe(wav_path)

    run_pipeline(
        transcript=transcript,
        out_image=str(dataDir / "output" / "output.png"),
        )



if __name__ == "__main__":
    main()