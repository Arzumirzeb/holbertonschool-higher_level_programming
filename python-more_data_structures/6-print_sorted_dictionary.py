#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for word, value in sorted(a_dictionary.items()):
        print(f"{word}: {value}")
