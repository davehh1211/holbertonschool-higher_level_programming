#!/usr/bin/python3
"""[summary]
    """
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    fullurl = 'https://api.github.com/repos/' + \
        sys.argv[1] + "/" + sys.argv[2] + "/commits"
    r = requests.get(fullurl)
    sha = r.json()[i].get('sha')
    user_com = r.json()[i].get('commit').get('author').get('name')
    print("{}: {}".format(sha, user_com))
