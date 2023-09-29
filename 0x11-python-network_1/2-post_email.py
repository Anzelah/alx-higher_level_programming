#!/usr/bin/python3
"""Defines a module"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = 'sys.argv[2]'
    email = email.encode('ascii')
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as res:
        content = res.read()
        print("{}" .format(content.decode("utf=8")))
