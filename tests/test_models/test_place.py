#!/usr/bin/python3
"""
This module defines unittests for the Place class
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Unit tests for the Place class.
    """

    def test_default_values(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_custom_values(self):
        city_id = "12345"
        user_id = "67890"
        name = "MyPlace"
        description = "A cozy place"
        number_rooms = 2
        number_bathrooms = 1
        max_guest = 4
        price_by_night = 100
        latitude = 40.7128
        longitude = -74.0060
        amenity_ids = ["1", "2", "3"]
        place = Place(city_id=city_id, user_id=user_id, name=name,
                      description=description, number_rooms=number_rooms,
                      number_bathrooms=number_bathrooms, max_guest=max_guest,
                      price_by_night=price_by_night, latitude=latitude,
                      longitude=longitude, amenity_ids=amenity_ids)
        self.assertEqual(place.city_id, city_id)
        self.assertEqual(place.user_id, user_id)
        self.assertEqual(place.name, name)
        self.assertEqual(place.description, description)
        self.assertEqual(place.number_rooms, number_rooms)
        self.assertEqual(place.number_bathrooms, number_bathrooms)
        self.assertEqual(place.max_guest, max_guest)
        self.assertEqual(place.price_by_night, price_by_night)
        self.assertEqual(place.latitude, latitude)
        self.assertEqual(place.longitude, longitude)
        self.assertEqual(place.amenity_ids, amenity_ids)

    def test_update_attribute(self):
        place = Place()
        place.city_id = "54321"
        self.assertEqual(place.city_id, "54321")

    def test_to_dict(self):
        place = Place(city_id="12345", user_id="67890", name="MyPlace",
                      description="A cozy place", number_rooms=2,
                      number_bathrooms=1, max_guest=4, price_by_night=100,
                      latitude=40.7128, longitude=-74.0060,
                      amenity_ids=["1", "2", "3"])
        place_dict = place.to_dict()
        self.assertIn("id", place_dict)
        self.assertIn("city_id", place_dict)
        self.assertIn("user_id", place_dict)
        self.assertIn("name", place_dict)
        self.assertIn("description", place_dict)
        self.assertIn("number_rooms", place_dict)
        self.assertIn("number_bathrooms", place_dict)
        self.assertIn("max_guest", place_dict)
        self.assertIn("price_by_night", place_dict)
        self.assertIn("latitude", place_dict)
        self.assertIn("longitude", place_dict)
        self.assertIn("amenity_ids", place_dict)
        self.assertEqual(place_dict["city_id"], "12345")
        self.assertEqual(place_dict["user_id"], "67890")
        self.assertEqual(place_dict["name"], "MyPlace")
        self.assertEqual(place_dict["description"], "A cozy place")
        self.assertEqual(place_dict["number_rooms"], 2)
        self.assertEqual(place_dict["number_bathrooms"], 1)
        self.assertEqual(place_dict["max_guest"], 4)
        self.assertEqual(place_dict["price_by_night"], 100)
        self.assertEqual(place_dict["latitude"], 40.7128)
        self.assertEqual(place_dict["longitude"], -74.0060)
        self.assertEqual(place_dict["amenity_ids"], ["1", "2", "3"])


if __name__ == "__main__":
    unittest.main()
