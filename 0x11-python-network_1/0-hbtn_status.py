#!/usr/bin/python3
"""Defines a module"""

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    page = res.read()
