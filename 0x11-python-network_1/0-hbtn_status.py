#!/usr/bin/python3
# This is a simple python3 script that fetches an HTTP url
import urllib.request as url


if __name__ == "__main__":
    # fetches https://alx-intranet.hbtn.io/status
    with url.urlopen('https://alx-intranet.hbtn.io/status') as f:
        body = f.read()
        body_utf = body.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body_utf))
