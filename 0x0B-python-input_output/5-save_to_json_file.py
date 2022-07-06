#!/usr/bin/python3
'''module for save_to_json_file'''

import json


def save_to_json_file(my_obj, filename):
    """function that writes an Obj to a text file,
    using JSON representation"""

    with open(filename, 'w') as f:
        filename = f.write(json.dumps(my_obj))
    return filename
