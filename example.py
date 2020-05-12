#!/usr/bin/env python3
from pathlib import Path
from lockfile import Lock
import time


def main() -> None:
    path = Path("example.txt")
    with Lock(path):
        time.sleep(10)  # to demonstrate the Lock (run it in parallel)
        with open(path, "w") as f:
            f.write("Hello!")


if __name__ == "__main__":
    main()
