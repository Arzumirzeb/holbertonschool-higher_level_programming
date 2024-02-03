#!/usr/bin/python3
"""Integer addition"""


def add_integer(a, b=98):
    """Algorithm for adding 2 integer"""
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
