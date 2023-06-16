#!/usr/bin/python3
""" a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8) 
"""
import urllib.request
import sys


if __name__ == "__main__":
    """ Takes the URL and sends a POST request with the email as parameter """
    get_url = sys.argv[1]
    val = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(val)
    data = data.encode('ascii')
    request = urllib.request.Request(get_url, data)
    with urllib.request.urlopen(request) as f:
        body = f.read()
        body_utf = body.decode('utf-8')
    print(body_utf)
