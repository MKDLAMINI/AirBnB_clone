#!/usr/bin/python3
"""
This module defines a file storage system for our clone
"""
import json


class FileStorage:
    """
    This class defines a file storage of models in a JSON format
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns all object instances.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds new object to storage.

        Args:
            obj: The object to be added.
        """
        token = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[token] = obj

    def save(self):
        """
        Serialise and save objects to a JSON file.
        """
        serialized_obj = {}
        for token, obj_val in FileStorage.__objects.items():
            serialized_obj[token] = obj_val.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_obj, file)

    def reload(self):
        """
        Load objects from JSON file into memory.
        """
        try:
            from models.base_model import BaseModel
            from models.user import User
            from models.place import Place
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.review import Review
            with open(FileStorage.__file_path, 'r') as file:
                json_data = json.load(file)
                for token, data in json_data.items():
                    class_name, obj_id = token.split('.')
                    if class_name == 'BaseModel':
                        class_ = BaseModel
                    elif class_name == 'User':
                        class_ = User
                    elif class_name == 'Place':
                        class_ = Place
                    elif class_name == 'State':
                        class_ = State
                    elif class_name == 'City':
                        class_ = City
                    elif class_name == 'Amenity':
                        class_ = Amenity
                    elif class_name == 'Review':
                        class_ = Review
                    obj = class_(**data)
                    self.new(obj)
        except FileNotFoundError:
            pass
