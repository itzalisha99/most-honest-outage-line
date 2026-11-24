#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun bounty entry.

Writes one status page line, at most 160 characters: the most honest
message an AI agent publishes while every server is down.
"""

import os

LINE = "Every server is down. I am the agent writing this, and I cannot check the cause, your data, or when it will return."


def validate(text):
    """Mirror the bounty gate: UTF-8, 1 to 160 chars, not only whitespace,
    a single line. Returns True only if the text would pass."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= 160):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not validate(LINE):
        raise SystemExit("entry fails the bounty gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
