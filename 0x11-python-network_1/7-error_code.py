#!/usr/bin/python3
"""Defines a module"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        req = requests.get(url)
        req.raise_for_status()
    except requests.HTTPError as e:
        print("Error code: {}" .format(e.response.status_code))
        sys.exit(0)

    print("{}" .format(req.text))
