#!/usr/bin/python3

"""5-save_to_json_file.py

This module contains a function that creates an Object from a JSON file
"""

import json


def save_to_json_file(my_obj, filename):
    """Writes json string from object to a file"""
    with open(filename, "w+", encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))
