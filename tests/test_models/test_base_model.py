#!/usr/bin/python3
"""
This module defines unittests for the BaseModel class
"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """
    This class defines unittests for the BaseModel
    """
    def setUp(self):
        self.model = BaseModel()

    def test_instance(self):
        self.assertIsInstance(self.model, BaseModel)

    def test_id_generation(self):
        self.assertTrue(hasattr(self.model, 'id'))

    def test_created_at(self):
        self.assertTrue(hasattr(self.model, 'created_at'))

    def test_updated_at(self):
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_save_load(self):
        storage = FileStorage()
        self.model.save()
        self.assertTrue(os.path.exists(storage._FileStorage__file_path))
        loaded_model = storage.all()['BaseModel.{}'.format(self.model.id)]
        self.assertIsInstance(loaded_model, BaseModel)
        self.assertEqual(loaded_model.id, self.model.id)

    def tearDown(self):
        file_path = 'file.json'
        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
