#!/usr/bin/python3

"""Write to a file"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        result = f.write(text)
    f.close()
    return result
