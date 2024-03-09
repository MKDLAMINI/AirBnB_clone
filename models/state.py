#!/usr/bin/python3
"""
Defines the state class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.

    Args:
        name (str, optional): The name of the state. Defaults to "".
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new State instance.
        """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get("name", "")
