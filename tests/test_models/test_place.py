"""Unittest for Place class."""
import unittest
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):
    """Class to test the Place class."""

    def setUp(self):
        """Create an instance of Place to use in tests."""
        self.place = Place()

    def tearDown(self):
        """Delete the instance of Place after tests."""
        del self.place

    def test_place_inherits_from_base_model(self):
        """Test that Place is a subclass of BaseModel."""
        self.assertIsInstance(self.place, BaseModel)

    def test_place_has_attributes(self):
        """Test that Place has the required class attributes."""
        attributes = ["city_id", "user_id", "name", "description", "number_rooms", "number_bathrooms", "max_guest", "price_by_night", "latitude", "longitude", "amenity_ids"]
        for attr in attributes:
            self.assertTrue(hasattr(Place, attr))

    def test_attributes_are_correct_type(self):
        """Test that the type of the attributes is correct."""
        self.assertEqual(type(Place.city_id), str)
        self.assertEqual(type(Place.user_id), str)
        self.assertEqual(type(Place.name), str)
        self.assertEqual(type(Place.description), str)
        self.assertEqual(type(Place.number_rooms), int)
        self.assertEqual(type(Place.number_bathrooms), int)
        self.assertEqual(type(Place.max_guest), int)
        self.assertEqual(type(Place.price_by_night), int)
        self.assertEqual(type(Place.latitude), float)
        self.assertEqual(type(Place.longitude), float)
        self.assertEqual(type(Place.amenity_ids), list)

    def test_attributes_are_default_values(self):
        """Test that the default value of the attributes is correct."""
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])
