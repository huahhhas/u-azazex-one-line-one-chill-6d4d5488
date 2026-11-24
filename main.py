#!/usr/bin/env python3
"""One Line, One Chill — writes a single horror line to /output/entry.txt."""
import os

LINE = "I found my own obituary in tomorrow's paper, and the cause of death was still blank."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
