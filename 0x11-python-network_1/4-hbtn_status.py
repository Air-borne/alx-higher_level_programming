#!/usr/bin/python3
# This is a simple python3 script that fetches an HTTP url using requests
import requests


if __name__ == "__main__":
    # fetches https://alx-intranet.hbtn.io/status using requests
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(response.text))
    print("\t- content: {}".format(body))
