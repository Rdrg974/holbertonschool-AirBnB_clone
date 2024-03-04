#!/usr/bin/python3
"""File storage class."""
import json


class FileStorage:
    """File storage class."""
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

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
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

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
