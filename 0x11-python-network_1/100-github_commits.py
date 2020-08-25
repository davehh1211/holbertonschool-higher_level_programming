#!/usr/bin/python3
"""[summary]
    """
import requests
import sys


if __name__ == "__main__":
    fullurl = 'https://api.github.com/repos/' + \
        sys.argv[2] + "/" + sys.argv[1] + "/commits"
    r = requests.get(fullurl)

    fileno = r.json()
    for item in fileno[:10]:
        sha = item.get('sha')
        user_com = item.get('commit').get('author').get('name')
        print("{}: {}".format(sha, user_com))
