#!/usr/bin/python3
"""Function for prints a text with characters: ., ? and :"""


def text_indentation(text):
    """Defines function for printgs text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    print("\n".join(a.strip() for a in text.split("\n")), end="")
