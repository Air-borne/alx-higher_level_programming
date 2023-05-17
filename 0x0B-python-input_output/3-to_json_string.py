#!/usr/bin/python3

"""3-to_json_string.py

This module contains a function that returns
the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """Returns the json representation of an object"""
    return json.dumps(my_obj)
