#!/usr/bin/python3
"""Sends a
POST request to the passed URL with the email
as a parameter
"""

from sys import argv
import requests


if __name__ == "__main__":
    payload = {'email': argv[2]}
    req = requests.post(argv[1], data=payload)

    print(req.text)
