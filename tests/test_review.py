#!/usr/bin/python3
"""
This module defines unittests for the Review class
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Unit tests for the Review class."""

    def test_default_values(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_custom_values(self):
        place_id = "12345"
        user_id = "67890"
        text = "Great place, highly recommended!"
        review = Review(place_id=place_id, user_id=user_id, text=text)
        self.assertEqual(review.place_id, place_id)
        self.assertEqual(review.user_id, user_id)
        self.assertEqual(review.text, text)

    def test_update_attribute(self):
        review = Review()
        review.place_id = "54321"
        self.assertEqual(review.place_id, "54321")

    def test_to_dict(self):
        review = Review(place_id="12345", user_id="67890",
                        text="Great place, highly recommended!")
        review_dict = review.to_dict()
        self.assertIn("id", review_dict)
        self.assertIn("place_id", review_dict)
        self.assertIn("user_id", review_dict)
        self.assertIn("text", review_dict)
        self.assertEqual(review_dict["place_id"], "12345")
        self.assertEqual(review_dict["user_id"], "67890")
        self.assertEqual(review_dict["text"],
                         "Great place, highly recommended!")


if __name__ == "__main__":
    unittest.main()
