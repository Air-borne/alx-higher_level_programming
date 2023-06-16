#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
"""
import urllib.request as url
import urllib
import sys


if __name__ == "__main__":
    """  Python script that takes in a URL, sends a request to the URL and displays the b         ody of the response (decoded in utf-8). 
    """
    get_url = sys.argv[1]
    request = url.Request(get_url)
    try:
        with urllib.request.urlopen(request) as f:
            body = f.read()
            body_utf = body.decode('utf-8')
            print(body_utf)
    except urllib.error.HTTPError as a:
        print("Error code: {}".format(a.code))
