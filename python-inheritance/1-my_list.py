#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """Define MyList class"""
    def print_sorted(self):
        """Print a list"""
        print(sorted(self))
