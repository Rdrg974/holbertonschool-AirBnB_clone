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
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """save method"""
        obj = {}
        for key, value in self.__objects.items():
            obj[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj, f)

    def reload(self):
        """reload method"""
        from models import base_model

        dict_module = {'BaseModel': base_model}

        try:
            with open(self.__file_path, 'r') as f:
                loard_objects = json.load(f)
                for key, value in loard_objects.items():
                    class_name = value['__class__']
                    if class_name in dict_module:
                        model_module = dict_module[class_name]
                        model_class = getattr(model_module, class_name)
                    self.__objects[key] = model_class(**value)
        except FileNotFoundError:
            pass
