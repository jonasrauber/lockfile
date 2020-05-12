#!/usr/bin/env python3
from pathlib import Path
from lockfile import Lock
import time


def main() -> None:
    path = Path("example.txt")
    with Lock(path):
        print("sleeping for 10s to demonstrate the Lock (run example.py in parallel)")
        time.sleep(10)
        with open(path, "w") as f:
            f.write("Hello!")


if __name__ == "__main__":
    main()
