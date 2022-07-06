#!/usr/bin/python3
'''module for load from json file'''

import json


def load_from_json_file(filename):
    """creates an Object from JSON file"""

    with open(filename) as f:
        return json.loads(f.read())
