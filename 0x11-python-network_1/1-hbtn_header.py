#!/usr/bin/python3
# This is a simple python3 script that receive the url and returns the X-Request-ID
import urllib.request as url
import sys


if __name__ == "__main__":
    """  accepts the url from the user 
    and return the body id using the get method
    """
    user_input = sys.argv[1]
    with url.urlopen(user_input) as f:
        body_id = f.info().get('X-Request-Id')
        print(body_id)
