#!/usr/bin/python3
"""Write a Python script that takes in a
letter and sends a POST request to
http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        dictjson = r.json()
        id_dictio = dictjson.get('id')
        name = dictjson.get('name')
        if len(dictjson) > 0 or id_dictio or name:
            print("[{}] {}".format(id_dictio, name))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
