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

    def __init__(self, name=""):
        """
        Start a new State instance.
        """
        super().__init__()
        self.name = name
