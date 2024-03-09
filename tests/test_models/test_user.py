#!/usr/bin/env python3
"""
This module defines unittests for the User class
"""
import os
import uuid
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Unit tests for the User class.
    """

    def setUp(self):
        """
        Set up a new User instance for each test.
        """
        self.name = "New user"
        self.user = User

    def test_first_name(self):
        """
        Test that first_name attribute is a string.
        """
        self.assertEqual(type(self.user.first_name), str)

    def test_last_name(self):
        """
        Test that last_name attribute is a string.
        """
        self.assertEqual(type(self.user.last_name), str)

    def test_email(self):
        """
        Test that email attribute is a string.
        """
        self.assertEqual(type(self.user.email), str)

    def test_password(self):
        """
        Test that password attribute is a string.
        """
        self.assertEqual(type(self.user.password), str)

    def test_default_values(self):
        """
        Test that default values are set correctly.
        """
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")

    def test_update_email(self):
        """
        Test updating the email attribute.
        """
        user = User()
        new_email = "new_email@example.com"
        user.email = new_email
        self.assertEqual(user.email, new_email)

    def test_update_password(self):
        """
        Test updating the password attribute.
        """
        user = User()
        new_password = "new_password"
        user.password = new_password
        self.assertEqual(user.password, new_password)

    def test_update_first_name(self):
        """
        Test updating the first_name attribute.
        """
        user = User()
        new_first_name = "John"
        user.first_name = new_first_name
        self.assertEqual(user.first_name, new_first_name)

    def test_update_last_name(self):
        """
        Test updating the last_name attribute.
        """
        user = User()
        new_last_name = "Doe"
        user.last_name = new_last_name
        self.assertEqual(user.last_name, new_last_name)

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
