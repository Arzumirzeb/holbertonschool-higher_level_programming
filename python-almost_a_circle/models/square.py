#!/usr/bin/python3

"""Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Define Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update square class"""
        if args and len(args) != 0:
            arguments = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, arguments[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary of objects"""
        new = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y}
        return new

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)
