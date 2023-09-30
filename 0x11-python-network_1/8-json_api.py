#!/usr/bin/python3
"""Defines a module"""

import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    q = {"q": letter}
    res = requests.post(url, q)

    try:
        req = res.json()
        if req:
            print("[{}}] {}" .format(req["id"], req["name"]))
        else:
            print("No result")
    except:
        print("Not a valid JSON")

