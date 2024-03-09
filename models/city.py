#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.

    Args:
        state_id (str, optional): The state id. Defaults to "".
        name (str, optional): The name of the city. Defaults to "".
    """
    state_id = ""
    name = ""

    def __init__(self, **kwargs):
        """Initializes a new City instance."""
        super().__init__(**kwargs)
        self.state_id = kwargs.get("state_id", "")
        self.name = kwargs.get("name", "")
