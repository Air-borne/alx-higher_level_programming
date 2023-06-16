#!/usr/bin/python3
""" 
Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header 
"""
import sys
import requests


if __name__ == "__main__":
    """
    Python script that takes in a URL, sends a request to the URL and displays the value     of the variable X-Request-Id in the response header
    """
    response = requests.get(sys.argv[1])
    try:
        response_id = response.headers['X-Request-Id']
        print(response_id)
    except:
        pass
