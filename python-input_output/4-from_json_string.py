#!/usr/bin/python3

"""From JSON string to Object"""


import json


def from_json_string(my_str):
    """Function that returns an object"""
    return json.loads(my_str)
