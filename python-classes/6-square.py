#!/usr/bin/python3
"""Define a class Square"""


class Square():
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializer for square class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """get the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set value for square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get the position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set value for position"""
        if not (isinstance(value, tuple) and len(value) == 2
            and isinstance(value[0], int) and value[0] >= 0
            and isinstance(value[1], int) and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

        def area(self):
            """Area of square"""
            return (self.__size * self.__size)

        def my_print(self):
            """Print square with (#)"""
            if self.__size == 0:
                print()
            else:
                for i in range(self.position[1]):
                    print()

                for i in range(self.size):
                    for j in range(self.position[0]):
                        print(" ", end="")
                    for k in range(self.__size):
                        print("#", end="")
                    print()
