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



def main():
    parser = argparse.ArgumentParser(
        description="Whisper → Stable Diffusion pipeline"
    )

    parser.add_argument(
        "audio",
        help="Path to the input audio file (wav/mp3/m4a/etc.)"
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

    print(f"[Whisper Loading model on {args.whisper_device}...]")
    whisper = WhisperClient(
        model_name="base.en",
        device=args.whisper_device,
        compute_type="int8"
    )

    print(f"[Whisper] Transcribing: {args.audio}")
    transcript = whisper.transcribe(args.audio)
    print(f"[Whisper] Transcript: \n{transcript}\n")

    # 2. Turn transcript into an image prompt 
    prompt = build_prompt(transcript, args.style_prefix)
    print(f"[Diffusion] Using prompt:\n{prompt}\n")

    # 3. Generate image
    print(f"[Diffusion] Loading pipeline on {args.device}...")
    diffusion = DiffusionClient(device=args.device)

    print(f"[Diffusion] Generating Image -> {args.out_image}")
    out_path = diffusion.generate(prompt, args.out_image)

    if out_path is None:
        print("[Diffusion] Generation failed.")
    else:
        print(f"[Done] Image saved to: {out_path}")


if __name__ == "__main__":
    main()