#!/usr/bin/python3
"""Post given email as parameter to given url"""
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    data = {"email": argv[2]}
    data = parse.urlencode(data).encode()
    my_request = request.Request(argv[1], data=data)
    with request.urlopen(my_request) as response:
        print(response.read().decode('utf-8'))
