#!/usr/bin/python3
"""Defines a module"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""

    payload = {"q": q}
    res = requests.post(url, data=payload)

    try:
        content = res.json()
        if len(content) == 0:
            print("No result")
            sys.exit()
        m_id = content.get('id')
        m_name = content.get('name')
        print("[{}] {}" .format(m_id, m_name))
    except ValueError:
        print("Not a valid JSON")
