#!/usr/bin/python3
"""Creates the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines the User class.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, **kwargs):
        """
        Start a new User instance.

        Args:
            kwargs (dict): A dictionary of attributes for the user.
        """
        super().__init__(**kwargs)
        self.email = kwargs.get("email", "")
        self.password = kwargs.get("password", "")
        self.first_name = kwargs.get("first_name", "")
        self.last_name = kwargs.get("last_name", "")
