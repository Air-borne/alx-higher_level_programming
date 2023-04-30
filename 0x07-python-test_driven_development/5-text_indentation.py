#!/usr/bin/python3

"""5-text_indentation.py
    This module contains a function 'text_indentation'
    you can test the function with the command

    python3 -m doctest -v ./test/5-text_indentation.txt
"""


def text_indentation(text):
    """Indents text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    indent = ""
    for c in text:
        indent += c
        if c in ".?:":
            print(f'{indent.strip(" ")}\n')
            indent = ""
    print(f'{indent.strip(" ")}', end='')
