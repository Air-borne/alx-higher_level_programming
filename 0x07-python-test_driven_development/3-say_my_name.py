#!/usr/bin/python3
"""3-say_my_name.py
    This module contains a function 'say_my_name'
    you can test the function with the command

    python3 -m doctest -v ./test/3-say_my_name.txt
"""


def say_my_name(first_name, last_name=""):
    """Prints a string containing arguments
    Args:
        first_name (str)
        last_name (str)
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
