#!/usr/bin/python3
"""Unittest for City class."""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Class to test the City class."""

    def setUp(self):
        """Create an instance of City to use in tests."""
        self.city = City()

    def tearDown(self):
        """Delete the instance of City after tests."""
        del self.city

    def test_city_inherits_from_base_model(self):
        """Test that City is a subclass of BaseModel."""
        self.assertIsInstance(self.city, BaseModel)

    def test_city_has_state_id_attribute(self):
        """Test that City has a class attribute state_id."""
        self.assertTrue(hasattr(City, "state_id"))

    def test_state_id_is_string(self):
        """Test that the type of state_id is str."""
        self.assertEqual(type(City.state_id), str)

    def test_state_id_is_empty_string(self):
        """Test that the default value of state_id is an empty string."""
        self.assertEqual(City.state_id, "")

    def test_city_has_name_attribute(self):
        """Test that City has a class attribute name."""
        self.assertTrue(hasattr(City, "name"))

    def test_name_is_string(self):
        """Test that the type of name is str."""
        self.assertEqual(type(City.name), str)

    def test_name_is_empty_string(self):
        """Test that the default value of name is an empty string."""
        self.assertEqual(City.name, "")
