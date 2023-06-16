#!/usr/bin/python3
"""Send a post request to a url, and checks if the response is valid json"""
import requests
from sys import argv

if __name__ == "__main__":
    q = ""
    if (len(argv) >= 2):
        q = argv[1]

    resp = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        body = resp.json()
        if (len(body) == 0):
            print('No result')
        else:
            print('[{}] {}'.format(body.get('id'), body.get('name')))
    except Exception as e:
        print('Not a valid JSON')
