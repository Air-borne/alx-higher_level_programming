#!/usr/bin/python3
"""This module contains a function that inserts a line of text to a file,
after each line containing a specific string (see example):
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends a string after a line if a pattern is found in said line"""
    myList = []
    with open(filename, "r", encoding="utf-8") as myFile:
        myList = myFile.readlines()
    with open(filename, "w", encoding="utf-8") as myFile:
        for elem in myList:
            myFile.write(elem)
            if (elem.find(search_string) >= 0):
                myFile.write(new_string)
