#!/usr/bin/python3

"""1-write_file.py

This module contains the function write_file that writes text to a file
"""


def write_file(filename="", text=""):
    """Writes text to given file"""
    with open(filename, "w+", encoding="utf-8") as myFile:
        myFile.write(text)
    return len(text)
