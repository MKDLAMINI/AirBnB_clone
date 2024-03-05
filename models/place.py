#!/usr/bin/python3
"""Defines a Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place.

    Args:
        city_id (str, optional): City id. Def to "".
        user_id (str, optional): User id. Def to "".
        description (str, optional): description of the place. Def to "".
        number_rooms (int, optional): num of rooms of the place. Def to 0.
        number_bathrooms (int, optional): bathroom num for the place. Def to 0.
        max_guest (int, optional): max num of guests of the place. Def to 0.
        price_by_night (int, optional): price by night of the place. Def to 0.
        latitude (float, optional): latitude of the place. Def to 0.0.
        longitude (float, optional): longitude of the place. Def to 0.0.
        amenity_ids (list, optional): A list of Amenity ids. Defaults to [].
    """

    def __init__(self, city_id="", user_id="", name="", description="",
                 number_rooms=0, number_bathrooms=0, max_guest=0,
                 price_by_night=0, latitude=0.0,
                 longitude=0.0, amenity_ids=[]):
        super().__init__()
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids
