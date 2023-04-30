#!/usr/bin/python3
"""5-square.py

This module contains a class Square that defines a square by:
(based on 4-square.py)


- Private instance attribute: size:

    - property def size(self): to retrieve it
    - property setter def size(self, value): to set it:

        - size must be an integer, otherwise raise a TypeError exception
          with the message 'size must be an integer'
        - if size is less than 0, raise a ValueError exception
          with the message 'size must be >= 0'

- Instantiation with optional size: def __init__(self, size=0):

- Public instance method:
    def area(self): that returns the current square area

-Public instance method:
    def my_print(self): that prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
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

    @property
    def size(self):
        """property method

        Returns:
            (int) - Size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter method

        Args:
            value (int): Size to set for the square.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the square area of the Square object

        Returns:
            (int) - Square area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints square to stdout"""
        if self.__size == 0:
            print('')
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print('')
