#!/usr/bin/python3
"""
A Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
"""
import requests as r
import sys


if __name__ == "__main__":
    """ 
    A Python script that takes in a URL and an email address, sends a POST request to the     passed URL with the email as a parameter, and finally displays the body of the respo     nse.
    """
    get_url = sys.argv[1]
    response = r.post(url, data={'email': sys.argv[2]})
    print(response.text)
