#!/usr/bin/python3
"""Module for User unittests."""
import unittest

from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test User class."""
    def test_user_email(self):
        """Test User.email"""
        user = User()
        self.assertNotEqual(user.email, None)

    def test_user_pwd(self):
        """Test User.password"""
        user = User()
        self.assertNotEqual(user.password, None)

    def test_user_firstname(self):
        """Test User.first_name"""
        user = User()
        self.assertNotEqual(user.first_name, None)

    def test_user_lastname(self):
        """Test User.last_name"""
        user = User()
        self.assertNotEqual(user.last_name, None)


if __name__ == "__main__":
    unittest.main()
