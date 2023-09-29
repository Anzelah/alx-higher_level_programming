#!/usr/bin/python3
"""Defines a module"""

import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    data = r.text
    print("Body response:")
    print("\t- type: {}" .format(type(data)))
    print("\t- content: {}" .format(data))
