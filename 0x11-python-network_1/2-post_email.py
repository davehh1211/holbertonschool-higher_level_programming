#!/usr/bin/python3
"""
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    dataset = urllib.parse.urlencode(values)
    dataset = dataset.encode('ascii')
    req = urllib.request.Request(sys.argv[1], dataset)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf8'))
