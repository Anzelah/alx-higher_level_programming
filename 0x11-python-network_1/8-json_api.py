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

    data = {"q": letter}
    res = requests.post(url, data)

    try:
        req = res.json()
        if (len(req) < 1):
            print("No results")
        else:
            print("[{}}] {}" .format(req["id"], req["name"]))
    except:
        print("Not a valid JSON")

