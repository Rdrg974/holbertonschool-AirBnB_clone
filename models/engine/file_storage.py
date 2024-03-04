#!/usr/bin/python3
"""File storage class."""
import json

class FileStorage:
    """File storage class."""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            for key, value in self.__objects.items():
                self.__objects[key] = value.to_dict()
                json.dump(self.__objects, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except:
            pass
