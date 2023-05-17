#!/usr/bin/python3

"""6-load_from_json_file.py

This module contains a function that creates an Object from a JSON file
"""

import json


def load_from_json_file(filename):
    """Loads object from json file"""
    with open(filename, "r", encoding="utf-8") as myFile:
        return json.loads(myFile.read())
