#!/usr/bin/env python3
"""Write one out-of-office auto-reply, as if a houseplant sent it.

Revision 2: sharper punch than revision 1. The plant's human left in
March and took the watering can, so the plant now runs on sunlight
and spite -- "photosynthesizing spite" carries the joke, and
"replies may wilt" lands it in plant terms instead of office cliche.
"""
import os

LINE = "Out of office: my human left in March and took the watering can. I'm photosynthesizing spite now \u2014 replies may wilt."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
