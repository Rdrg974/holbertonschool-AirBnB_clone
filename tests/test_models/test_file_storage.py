#!/usr/bin/python3
"""Module for File Storage unittests."""
import json
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Tests File Storage class."""
    def test_objects(self):
        """Test __objects"""
        storage = FileStorage()
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_all(self):
        """Test all()"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertIsInstance(new_dict, dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    def test_new(self):
        """Test new()"""
        storage = FileStorage()
        my_model = BaseModel()
        storage.new(my_model)
        self.assertIn("BaseModel." + my_model.id, storage._FileStorage__objects)

    def test_save(self):
        """Test save()"""
        storage = FileStorage()
        my_model = BaseModel()
        storage.new(my_model)
        storage.save()
        with open("file.json", "r") as f:
            self.assertEqual(json.load(f), storage._FileStorage__objects)

    def test_reload(self):
        """Test reload()"""
        storage = FileStorage()
        my_model = BaseModel()
        storage.new(my_model)
        storage.save()
        storage.reload()
        self.assertIn("BaseModel." + my_model.id, storage._FileStorage__objects)
        with open("file.json", "r") as f:
            self.assertEqual(json.load(f), storage._FileStorage__objects)

    def test__init__(self):
        """Test __init__()"""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_save2(self):
        """Test save()"""
        storage = FileStorage()
        my_model = BaseModel()
        storage.new(my_model)
        storage.save()
        with open("file.json", "r") as f:
            self.assertEqual(json.load(f), storage._FileStorage__objects)

if __name__ == "__main__":
    unittest.main()
