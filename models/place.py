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
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Place instance.
        """
        super().__init__(*args, **kwargs)
        self.city_id = kwargs.get("city_id", "")
        self.user_id = kwargs.get("user_id", "")
        self.name = kwargs.get("name", "")
        self.description = kwargs.get("description", "")
        self.number_rooms = kwargs.get("number_rooms", 0)
        self.number_bathrooms = kwargs.get("number_bathrooms", 0)
        self.max_guest = kwargs.get("max_guest", 0)
        self.price_by_night = kwargs.get("price_by_night", 0)
        self.latitude = kwargs.get("latitude", 0.0)
        self.longitude = kwargs.get("longitude", 0.0)
        self.amenity_ids = kwargs.get("amenity_ids", [])
