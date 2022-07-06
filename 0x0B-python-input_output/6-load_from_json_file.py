#!/usr/bin/python3

import json


def load_from_json_file(filename):
    """creates an Obj from a “JSON file”"""
    with open(filename, "r", encoding="utf-8") as content:
        return json.load(content)
