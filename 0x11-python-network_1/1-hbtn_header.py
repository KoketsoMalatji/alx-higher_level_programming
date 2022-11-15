#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
"""
import urllib.request
import sys

if __name__ == "__main__":
    argument = sys.argv[1]
    with urllib.request.urlopen(argument) as response:
        print(response.headers['X-Request-Id'])
