#!/usr/bin/python3
"""Module for File Storage unittests."""
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
        file_storage = FileStorage()
        my_model = BaseModel()
        file_storage.new(my_model)
        self.assertIn("BaseModel." + my_model.id, file_storage._FileStorage__objects)

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
        file_storage = FileStorage()
        my_model = BaseModel()
        my_model.save()
        file_storage.reload()
        new_dict = file_storage.all()
        self.assertIn("BaseModel." + my_model.id, new_dict)

if __name__ == "__main__":
    unittest.main()
