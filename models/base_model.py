#!/usr/bin/python3
"""
This module defines a base class for our models in the clone.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    The base class for all our bnb models
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        bnb_dict = {}
        bnb_dict = self.__dict__.copy()
        bnb_dict['__class__'] = self.__class__.__name__
        bnb_dict['created_at'] = self.created_at.isoformat()
        bnb_dict['updated_at'] = self.updated_at.isoformat()
        return bnb_dict
