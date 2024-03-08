#!/usr/bin/python3
"""Module for Amenity unittests."""
import unittest

from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Class to test the Amenity class."""

    def setUp(self):
        """Create an instance of Amenity to use in tests."""
        self.amenity = Amenity()

    def tearDown(self):
        """Delete the instance of Amenity after tests."""
        del self.amenity

    def test_amenity_inherits_from_base_model(self):
        """Test that Amenity is a subclass of BaseModel."""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenity_has_name_attribute(self):
        """Test that Amenity has a class attribute name."""
        self.assertTrue(hasattr(Amenity, "name"))

    def test_name_is_string(self):
        """Test that the type of name is str."""
        self.assertEqual(type(Amenity.name), str)

    def test_name_is_empty_string(self):
        """Test that the default value of name is an empty string."""
        self.assertEqual(Amenity.name, "")


if __name__ == "__main__":
    unittest.main()
