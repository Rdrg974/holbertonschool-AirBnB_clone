#!/usr/bin/python3
"""File storage class."""
import json


class FileStorage:
    """File storage class."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all method
        Returns:
            [dict]: __objects"""
        return self.__objects

    def new(self, obj):
        """new method"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """save method"""
        new_dict = {obj: self.__objects[obj].to_dict() for obj in self.__objects}
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """reload method"""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
                for value in self.__objects.values():
                    class_name = value['__class__']
                    del value['__class__']
                    self.new(eval(class_name)(**value))
        except Exception:
            pass
