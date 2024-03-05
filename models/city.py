#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.

    Args:
        state_id (str, optional): The state id. Defaults to "".
        name (str, optional): The name of the city. Defaults to "".
    """

    def __init__(self, state_id="", name=""):
        """Starts a new City instance."""
        super().__init__()
        self.state_id = state_id
        self.name = name
