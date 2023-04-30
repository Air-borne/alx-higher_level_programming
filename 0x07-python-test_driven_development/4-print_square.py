#!/usr/bin/python3
"""4-print_square.py
    This module contains a function 'print_square'
    you can test the function with the command

    python3 -m doctest -v ./test/4-print_square.txt
"""


def print_square(size):
    """Prints a square with the character #
    Args:
        size (int): size of the square
    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
