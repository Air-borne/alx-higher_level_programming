#!/usr/bin/python3
"""1-square.py

This module contains a class Square that defines a square by:
(based on 0-square.py)

- Private instance attribute: size
- Instantiation with size (no type/value verification)

"""


class Square():
    """Defines a square"""

    def __init__(self, size=0):
        """Sets attributes for a Square object when it is instanciated

            Args:
                size (int): Size of all sides of the square.
        """
        self.__size = size
