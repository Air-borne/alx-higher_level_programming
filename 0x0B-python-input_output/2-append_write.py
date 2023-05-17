#!/usr/bin/python3

"""2-append_write.py

This module contains the function append_write that append text to a file
"""


def append_write(filename="", text=""):
    """Appends text onto given file"""
    with open(filename, "a+", encoding="utf-8") as myFile:
        myFile.write(text)
    return len(text)
