#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """Define function"""
    return type(obj) is not a_class and isinstance(obj, a_class)
