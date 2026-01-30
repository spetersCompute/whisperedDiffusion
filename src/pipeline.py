import argparse
from src.whisper_client import WhisperClient
from src.diffusion_client import DiffusionClient


def build_prompt(transcript: str, prefix: str | None) -> str:
    """
    Take the raw transcript and optionally prepend a style prefix
    """
    transcript = transcript.strip()

    if prefix: 
        return f"{prefix.strip()} {transcript}"
    return transcript

def run_pipeline(
    transcript: str,
    out_image: str = "output.png",
    device: str = "cpu",
    whisper_device: str = "cpu",
    style_prefix: str = "A vibrant neon synthwave illustration of",
):
    print(f"[Whisper Loading model on {whisper_device}...]")
    whisper = WhisperClient(
        model_name="base.en",
        device=whisper_device,
        compute_type="int8"
    )
    # Function: transcript -> prompt -> diffusion
    transcript  = transcript.strip()
    print(f"[Whisper] Transcript: \n{transcript}\n")

    prompt = build_prompt(transcript, style_prefix)
    print(f"[Diffusion] Using prompt: \n{prompt}\n")

    print(f"[Diffusion] Loading pipeline on {device}...")
    diffusion = DiffusionClient(device=device)

    print(f"[Diffusion] Generating Image -> {out_image}")
    out_path = diffusion.generate(prompt, out_image)

    if out_path is None:
        print("[Diffusion] Generation failed.")
    else: 
        print(f"[Done] Image saved to: {out_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Whisper → Stable Diffusion pipeline"
    )

    parser.add_argument(
        "--out-image",
        "-o",
        default="output.png",
        help="Path to save the generated image (default: output.png)"
    )

    parser.add_argument(
        "--device",
        "-d",
        default="cpu",
        choices=["cpu", "cuda"],
        help="Device for diffusion (default:cpu)",
    )

    parser.add_argument(
        "--whisper-device",
        default="cpu",
        choices=["cpu", "cuda"],
        help="device for Whisper (default:cpu)"
    )

    parser.add_argument(
        "--style-prefix",
        default="A vibrant neon cyberpunk illustration of",
        help=(
            "Optional text to prepend to the transcript to turn it into "
            "an image prompt."
        )
    )

    args = parser.parse_args()

    # 1. Transcribe audio --> Text

    transcript = input("Say prompt text: ")

    run_pipeline(
        transcript=transcript,
        out_image=args.out_image,
        device=args.device,
       whisper_device=args.whisper_device,
       style_prefix=args.style_prefix, 
    )



if __name__ == "__main__":
    main()