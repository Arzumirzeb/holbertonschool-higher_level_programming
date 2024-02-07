#!/usr/bin/python3
""" My class module """


def class_to_json(obj):
    """Function that returns the dictionary description"""
    return obj.__dict__
