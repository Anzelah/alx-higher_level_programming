#!/usr/bin/python3
"""Defines a module"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        content = res.getheader("X-Request-Id")
        print("{}" .format(content))
