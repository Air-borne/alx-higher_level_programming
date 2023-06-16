#!/usr/bin/python3
"""Display body of given url, or error code if there is an error"""
from urllib import request, error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as exception:
        print('Error code: {}'.format(exception.code))
