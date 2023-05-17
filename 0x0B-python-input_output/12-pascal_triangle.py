#!/usr/bin/python3
"""This module contains a function def pascal_triangle(n):
that returns a list of lists of integers representing the Pascal’s
triangle of n:
"""


def pascal_triangle(n):
    """Returns pascal's triangle at index n"""
    myList = []
    myListofLists = []
    for i in range(n):
        myTmpList = []
        if i >= 2:
            for j in range(len(myList)):
                if j == 0:
                    myTmpList.append(1)
                else:
                    myTmpList.append(myList[j] + myList[j - 1])
            myList = myTmpList.copy()
        myList.append(1)
        myListofLists.append(myList.copy())
    return myListofLists
