#!/usr/bin/python3
"""Display value of a variable in header of given URL"""
import requests
from sys import argv

if __name__ == "__main__":
    resp = requests.get(argv[1])
    print(resp.headers.get('X-Request-Id'))
