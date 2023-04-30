#!/usr/bin/python3
"""2-square.py

This module contains a class Square that defines a square by:
(based on 0-square.py)

- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0):
    - size must be an integer, otherwise raise a TypeError exception
      with the message size must be an integer
    - if size is less than 0, raise a ValueError exception with the message
      'size must be >= 0'

"""


class Square():
    """Defines a square"""

    def __init__(self, size=0):
        """Sets attributes for a Square object when it is instanciated

            Args:
                size (int): Size of all sides of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
