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

if __name__ == "__main__":
    unittest.main()
