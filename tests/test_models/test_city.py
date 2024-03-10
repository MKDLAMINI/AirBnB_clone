#!/usr/bin/env python3
"""
This module runs unittests on the City class
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Unit tests for the City class.
    """

    def test_default_values(self):
        """
        Test if default values are set correctly.
        Checks if the City instance is initialized with default values
        for state_id and name attributes.
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_custom_values(self):
        """
        Test if custom values are set correctly.
        Checks if the City instance is initialized with custom values
        for state_id and name attributes.
        """
        state_id = "12345"
        name = "New York"
        city = City(state_id=state_id, name=name)
        self.assertEqual(city.state_id, state_id)
        self.assertEqual(city.name, name)

    def test_update_attribute(self):
        city = City()
        city.state_id = "54321"
        self.assertEqual(city.state_id, "54321")

    def test_to_dict(self):
        city = City(state_id="1234567", name="Houston")
        city_dict = city.to_dict()
        self.assertIn("id", city_dict)
        self.assertIn("state_id", city_dict)
        self.assertIn("name", city_dict)
        self.assertIn("__class__", city_dict)
        self.assertEqual(city_dict["state_id"], "1234567")
        self.assertEqual(city_dict["name"], "Houston")
        self.assertEqual(city_dict["__class__"], "City")


if __name__ == "__main__":
    unittest.main()
