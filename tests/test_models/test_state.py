"""Unittest for the State class."""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Class to test the State class."""

    def setUp(self):
        """Create an instance of State to use in tests."""
        self.state = State()

    def tearDown(self):
        """Delete the instance of State after tests."""
        del self.state

    def test_state_inherits_from_base_model(self):
        """Test that State is a subclass of BaseModel."""
        self.assertIsInstance(self.state, BaseModel)

    def test_state_has_name_attribute(self):
        """Test that State has a class attribute name."""
        self.assertTrue(hasattr(State, "name"))

    def test_name_is_string(self):
        """Test that the type of name is str."""
        self.assertEqual(type(State.name), str)

    def test_name_is_empty_string(self):
        """Test that the default value of name is an empty string."""
        self.assertEqual(State.name, "")
