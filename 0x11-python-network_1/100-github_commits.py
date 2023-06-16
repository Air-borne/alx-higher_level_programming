#!/usr/bin/python3
"""
List 10 commits  of the repository “rails”
by the user “rails”
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    List 10 commits of the repository
    “rails” y the user “rails”
    """
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = requests.get(url)
    res_list = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(res_list[i].get('sha'), res_list[i].
                                  get('commit').get('author').get('name')))
    except:
        pass
