#!/usr/bin/python3
"""Defines a module"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            content = res.read()
            print("{}" .format(content.decode("utf=8")))
    except urllib.error.HTTPError as e:
        print("Error code: {}" .format(e.code))
