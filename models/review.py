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
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Review instance.
        """
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get("place_id", "")
        self.user_id = kwargs.get("user_id", "")
        self.text = kwargs.get("text", "")
