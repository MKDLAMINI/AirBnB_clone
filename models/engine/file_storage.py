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
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_obj = {}
        for key, obj_val in FileStorage.__objects.items():
            serialized_obj[key] = obj_val.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_obj, file)

    def reload(self):
        try:
            from models.base_model import BaseModel
            with open(FileStorage.__file_path, 'r') as file:
                json_data = json.load(file)
                for key, value in json_data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'BaseModel':
                        class_ = BaseModel
                    obj = class_(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass
