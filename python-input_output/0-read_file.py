#!/usr/bin/python3

"""Read file"""


def read_file(filename=""):
    """Function that reads a text file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
        f.close()
