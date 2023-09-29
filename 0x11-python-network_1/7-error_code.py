#!/usr/bin/python3
"""Defines a module"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        req = requests.get(url)
        content = req.text
        print("{}" .format(content))
    except requests.HTTPError as e:
        code = req.status_code
        if code >= 400:
            print("Error code: {}" .format(code))
