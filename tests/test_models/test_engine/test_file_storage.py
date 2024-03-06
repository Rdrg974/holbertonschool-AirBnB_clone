#!/usr/bin/python3
"""Module for File Storage unittests."""
import os
import json
import unittest

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests File Storage class."""
    def test_file_path(self):
        """Test __file_path"""
        file_storage = FileStorage()
        expected_file = 'file.json'
        self.assertEqual(file_storage._FileStorage__file_path, expected_file)

    def test_objects(self):
        """Test __objects"""
        file_storage = FileStorage()
        self.assertIsInstance(file_storage._FileStorage__objects, dict)

    def test_all(self):
        """Test all()"""
        file_storage = FileStorage()
        new_dict = file_storage.all()
        self.assertIsInstance(new_dict, dict)
        self.assertIs(new_dict, file_storage._FileStorage__objects)

    def test_new(self):
        """Test new()"""
        f_sto = FileStorage()
        my_model = BaseModel()
        f_sto.new(my_model)
        self.assertIn("BaseModel." + my_model.id, f_sto._FileStorage__objects)

    def test_save(self):
        """Test save()"""
        file_storage = FileStorage()
        my_model = BaseModel()
        file_storage.new(my_model)
        file_storage.save()
        with open('file.json', 'r') as f:
            json_dict = json.load(f)
        self.assertIn("BaseModel." + my_model.id, json_dict)

    def test_reload(self):
        """Test reload()"""
        self.assertTrue(os.path.exists("file.json"))
        my_model = BaseModel()
        file_storage = FileStorage()
        file_storage.new(self.model)
        file_storage.save()
        file_storage.reload()
        with open("file.json", 'r') as file:
            self.assertIn("BaseModel." + my_model.id, json.load(file))

        file_storage.save()
        file_storage._FileStorage__objects = {}
        file_storage.reload()
        self.assertNotEqual(self.storage.all(), {})


if __name__ == "__main__":
    unittest.main()
