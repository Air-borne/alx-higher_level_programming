#!/usr/bin/python3
"""Display value of a variable in header of given URL"""
from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
