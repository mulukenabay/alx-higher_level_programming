#!/usr/bin/python3
"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    """a function writes a string and return number of character"""
    with open(filename, "w" encoding="utf-8") as f:
	return f.write(text)
