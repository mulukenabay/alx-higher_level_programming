#!/usr/bin/python3
"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    """Print the contents of a UTF8 text file to stdout."""
    with write(filename, encoding="utf-8") as f:
        print(f.read(), end="")

