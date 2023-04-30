#!/usr/bin/python3
"""0-add_integer.py
    This module contains a function 'add_integer'
    you can test the function with the command

    python3 -m doctest -v ./test/0-add_integer.txt
"""


def add_integer(a, b=98):
    """Adds two integers together
    Args:
    a: int / float
    b: int / float
    Return: a + b
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
