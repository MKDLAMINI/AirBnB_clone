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
    def __init__(self, *args, **kwargs):
        """
        Updating current BaseModel instance.

        Args:
            *args (any): Unutilized
            **kwargs (dict): dict of attribute for making a new instance
        """
        if kwargs:
            self.id = kwargs.get("id")
            if not self.id:
                raise ValueError("Missing necessary attribute: id")

            self.created_at = datetime.fromisoformat(
                kwargs.get("created_at")
            ) or None

            if not self.created_at:
                raise ValueError("Missing necessary attribute: created_at")

            self.updated_at = datetime.fromisoformat(
                kwargs.get("updated_at")
            ) or None

            if not self.updated_at:
                raise ValueError("Missing necessary attribute: updated_at")

            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            from models import storage
            self.created_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        bnb_dict = {}
        bnb_dict = self.__dict__.copy()
        bnb_dict['__class__'] = self.__class__.__name__
        bnb_dict['created_at'] = self.created_at.isoformat()
        bnb_dict['updated_at'] = self.updated_at.isoformat()
        return bnb_dict
