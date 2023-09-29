#!/usr/bin/python3
"""Defines a module"""

import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    res = r.read()
    print("Body response:")
    print("\t- type: {}" .format(type(r)))
    print("\t- content: {}" .format(r))
