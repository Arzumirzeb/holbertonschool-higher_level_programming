#!/usr/bin/python3
"""Define a class Square"""


class Square():
    """Square class"""

    def __init__(self, size=0):
        """Initializer for square class"""
        self.__size = size

    @property
    def size(self):
        """get the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square with (#)"""
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()


