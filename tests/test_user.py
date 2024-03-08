#!/usr/bin/env python3
"""
This module defines unittests for the User class
"""
import uuid
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Unit tests for the User class.
    """

    def setUp(self):
        """Set up a new User instance for each test."""
        self.name = "New user"
        self.user = User

    def test_first_name(self):
        """Test that first_name attribute is a string."""
        self.assertEqual(type(self.user.first_name), str)

    def test_last_name(self):
        """Test that last_name attribute is a string."""
        self.assertEqual(type(self.user.last_name), str)

    def test_email(self):
        """Test that email attribute is a string."""
        self.assertEqual(type(self.user.email), str)

    def test_password(self):
        """Test that password attribute is a string."""
        self.assertEqual(type(self.user.password), str)

    def test_default_values(self):
        """Test that default values are set correctly."""
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")

    def test_custom_values(self):
        """Test that custom values are set correctly."""
        email = "test@example.com"
        custom_user = User(id="123", email=email)
        self.assertEqual(custom_user.email, email)

        password = "password123"
        custom_user = User(id="456", password=password)
        self.assertEqual(custom_user.password, password)

        first_name = "John"
        custom_user = User(id="789", first_name=first_name)
        self.assertEqual(custom_user.first_name, first_name)


if __name__ == "__main__":
    unittest.main()
