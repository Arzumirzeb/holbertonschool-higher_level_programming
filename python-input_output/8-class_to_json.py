#!/usr/bin/python3
""" My class module """


import json


def class_to_json(obj):
    """Function that returns the dictionary description"""
    return obj.__dict__
