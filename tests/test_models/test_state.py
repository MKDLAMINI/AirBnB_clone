#!/usr/bin/python3
"""
This module defines unittests for the State class
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Unit tests for the State class.
    """

    def test_default_values(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_custom_values(self):
        name = "Texas"
        state = State(name=name)
        self.assertEqual(state.name, name)

    def test_update_attribute(self):
        state = State()
        state.name = "Florida"
        self.assertEqual(state.name, "Florida")

    def test_to_dict(self):
        state = State(name="California")
        state_dict = state.to_dict()
        self.assertIn("id", state_dict)
        self.assertIn("name", state_dict)
        self.assertEqual(state_dict["name"], "California")
        self.assertEqual(state_dict["__class__"], "State")


if __name__ == "__main__":
    unittest.main()
