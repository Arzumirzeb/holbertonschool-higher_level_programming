#!/usr/bin/python3

"""Class Base"""


import json


class Base:
    """Define Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that
        returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that
        writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dicts = [i.to_dictionary() for i in list_objs]
                f.write(cls.to_json_string(dicts))
        f.close()

    @staticmethod
    def from_json_string(json_string):
        """Static method that
        returns the list of the JSON string
        representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that
        returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            new_instance = cls(1, 1)
        elif cls is Square:
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Class method that returns a list of instances"""
        try:
            with open(f"{cls.__name__}.json", "r", encoding="utf-8") as f:
                list_dict = cls.from_json_string(f.read())
            instances = []
            for d in list_dict:
                instances.append(cls.create(**d))
            return instances
            f.close()
        except Exception:
            return []
