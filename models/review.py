#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Args:
        place_id (str, optional): The Place id. Defaults to "".
        user_id (str, optional): The User id. Defaults to "".
        text (str, optional): The text of the review. Defaults to "".
    """

    def __init__(self, place_id="", user_id="", text=""):
        """Start a new Review instance."""
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
