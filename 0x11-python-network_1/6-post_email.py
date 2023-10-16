#!/usr/bin/python3
"""Defines a module"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    email = {"email": email}
    r = requests.get(url, params=email)
    req = requests.post(url, email)
    content = req.text
    print("{}" .format(content))
