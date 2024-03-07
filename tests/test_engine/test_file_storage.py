#!/usr/bin/python3
"""
This module defines unittests for FileStorage class
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        model = BaseModel()
        self.storage.new(model)
        key = '{}.{}'.format(model.__class__.__name__, model.id)
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_save(self):
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as f:
            data = f.read()
            self.assertTrue(data)

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
