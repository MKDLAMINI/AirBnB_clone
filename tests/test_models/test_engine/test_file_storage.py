#!/usr/bin/python3
"""
This module defines unittests for FileStorage class
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    This class defines unit tests for the FileStorage class
    """
    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        model = BaseModel()
        self.storage.new(model)
        key = '{}.{}'.format(model.__class__.__name__, model.id)
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as f:
            data = f.read()
            self.assertTrue(data)


if __name__ == '__main__':
    unittest.main()
