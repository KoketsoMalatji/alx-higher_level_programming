#!/usr/bin/python3
"""
Sends a request to the URL and
displays the body of the response
"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":

    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            resp = response.read()
            print(resp.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
