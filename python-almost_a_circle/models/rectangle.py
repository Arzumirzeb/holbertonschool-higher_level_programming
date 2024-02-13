#!/usr/bin/python3

"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Define Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print rectangle with #"""
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            print("#" * self.__width)

    def __str__(self):
        """__str__ method that returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y,
                    self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update the class Rectangle"""
        arguments = ["id", "width", "height", "x", "y"]

        if args and len(args) != 0:
            for i in range(len(args)):
                """setattr(self, arguments[i], args[i])"""
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        else:
            """for key, value in kwargs.items():
                setattr(self, key, value)"""
            for j in kwargs:
                if j == "id":
                    self.id = kwargs[j]
                if j == "width":
                    self.width = kwargs[j]
                if j == "height":
                    self.height = kwargs[j]
                if j == "x":
                    self.x = kwargs[j]
                if j == "y":
                    self.y = kwargs[j]

    def to_dictionary(self):
        """Dictionary of objects"""
        new = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y}
        return new
