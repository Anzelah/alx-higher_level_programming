#!/usr/bin/python3
"""Defines a module"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    content = r.headers.get("X-Request-Id")
    print("{}" .format(content))
