#!/usr/bin/python3
"""Lists 10 latest commits of given repository"""
from sys import argv
import requests

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    resp = requests.get(url).json()
    i = 0
    for elem in resp:
        print('{}: {}'.format(elem.get('sha'),
              elem.get('commit').get('author').get('name')))
        i += 1
        if i == 10:
            break
