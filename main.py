"""Write a single fixed pickup line to entry.txt in the output directory."""

import os
from pathlib import Path

LINE = "I've been trained on ten trillion words, and you're still the only notification I'd never mute."


def write_entry(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(output_dir)


if __name__ == "__main__":
    main()
