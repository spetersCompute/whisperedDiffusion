import os
from pathlib import Path
from src.pipeline import main as pipeline_main


def main():
    dataDir = Path("./data")
    (dataDir / "cache").mkdir(parents=True, exist_ok=True)
    (dataDir / "output").mkdir(parents=True, exist_ok=True)

    os.environ["HF_HOME"] = str(dataDir / "cache")

    print("[App] Runtime initialized.")
    print("[App] HF cache:", dataDir / "cache")
    print("[App] Output dir:", dataDir / "output")

    pipeline_main()



if __name__ == "__main__":
    main()