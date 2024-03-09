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
        if kwargs.get("id") is not None:
            self.id = kwargs.get("id")
        else:
            self.id = str(uuid.uuid4())

        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"

            self.created_at = datetime.strptime(
                kwargs.get('created_at', datetime.now().strftime(date_format)),
                date_format)
            self.updated_at = datetime.strptime(
                kwargs.get('updated_at', datetime.now().strftime(date_format)),
                date_format)

        else:
            from models import storage
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns string representation of the object.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Save the object to storage.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Convert the object into a dictionary representation.
        """
        bnb_dict = {}
        bnb_dict = self.__dict__.copy()
        bnb_dict['__class__'] = self.__class__.__name__
        bnb_dict['created_at'] = self.created_at.isoformat()
        bnb_dict['updated_at'] = self.updated_at.isoformat()
        return bnb_dict
