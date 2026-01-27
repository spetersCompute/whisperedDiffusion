import os
from pathlib import Path
from src.pipeline import run_pipeline


def main():
    dataDir = Path("./data")
    (dataDir / "cache").mkdir(parents=True, exist_ok=True)
    (dataDir / "output").mkdir(parents=True, exist_ok=True)

    os.environ["HF_HOME"] = str(dataDir / "cache")

    print("[App] Runtime initialized.")
    print("[App] HF cache:", dataDir / "cache")
    print("[App] Output dir:", dataDir / "output")

    transcript = input("say prompt text: ")
    run_pipeline(
        transcript=transcript,
        out_image=str(dataDir / "output" / "output.png")
        )



if __name__ == "__main__":
    main()