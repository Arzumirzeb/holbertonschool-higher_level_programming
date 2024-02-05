#!/usr/bin/python3
"""Rectangle class"""


class Rectangle():
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Define function for rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set value of width"""
        if not isinstance(value, int):
            raise TypeError("""width must be an integer""")
        if value < 0:
            raise ValueError("""width must be >= 0""")
        self.__width = value

    @property
    def height(self):
        """get value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value of height"""
        if not isinstance(value, int):
            raise TypeError("""height must be an integer""")
        if value < 0:
            raise ValueError("""height must be >= 0""")
        self.__height = value

    def area(self):
        """Define area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Define perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print rectangle"""
        end = ""
        if self.__width == 0 or self.__height == 0:
            return end

        for i in range(self.__height):
            for j in range(self.__width):
                end += "#"
            if i != self.__height - 1:
                end += '\n'
        return end
