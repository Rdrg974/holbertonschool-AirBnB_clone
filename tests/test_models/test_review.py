"""Unittest for Review class."""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Class to test the Review class."""

    def setUp(self):
        """Create an instance of Review to use in tests."""
        self.review = Review()

    def tearDown(self):
        """Delete the instance of Review after tests."""
        del self.review

    def test_review_inherits_from_base_model(self):
        """Test that Review is a subclass of BaseModel."""
        self.assertIsInstance(self.review, BaseModel)

    def test_review_has_attributes(self):
        """Test that Review has the required class attributes."""
        attributes = ["place_id", "user_id", "text"]
        for attr in attributes:
            self.assertTrue(hasattr(Review, attr))

    def test_attributes_are_correct_type(self):
        """Test that the type of the attributes is correct."""
        self.assertEqual(type(Review.place_id), str)
        self.assertEqual(type(Review.user_id), str)
        self.assertEqual(type(Review.text), str)

    def test_attributes_are_default_values(self):
        """Test that the default value of the attributes is correct."""
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
