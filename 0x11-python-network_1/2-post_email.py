#!/usr/bin/python3
"""Write a Python script that takes in a URL and
an email, sends a POST request to the passed URL
with the email as a parameter, and displays the
body of the response (decoded in utf-8)
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
