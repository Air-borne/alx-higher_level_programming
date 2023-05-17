#!/usr/bin/python3

"""0-read_file.py

This module contains a function read_file that reads a file and prints it
"""


def read_file(filename=""):
    """Prints given file to stdout"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
