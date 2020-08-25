#!/usr/bin/python3
"""[summary]
    """
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    fullurl = 'https://api.github.com/users/' + \
        sys.argv[1]
    r = requests.get(fullurl, auth=HTTPBasicAuth(sys.argv[1],
                                                 sys.argv[2]))
    print(r.json().get('id'))
