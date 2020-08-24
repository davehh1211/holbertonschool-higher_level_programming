#!/usr/bin/python3
"""[summary]
    """
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('x-request-id'))
