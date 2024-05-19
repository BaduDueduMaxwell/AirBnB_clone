#!/usr/bin/python3
""""""

import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up a new instance for testing"""
        self.model = BaseModel()

    def test_id(self):
        """Test if id is a string and unique"""
        self.assertIsInstance(self.model.id, str)
        self.assertEqual(len(self.id), 36)

    def test_created_at(self):
        """Test if created_at is set at initialization and is a datetime object"""
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertAlmostEqual(self.model.created_at, datetime.now(), delta=timedelta(seconds=1))

    def test_updated_at(self):
        """Test if updated_at is set at initialization and is a datetime object"""
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertAlmostEqual(self.model.updated_at, datetime.now(), delta=timedelta(seconds=1))
    
    def test_save_method(self):
        """Test if save method updates updated_at"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotAlmostEqual(old_updated_at, self.model.updated_at)
        self.assertTrue(self.model.updated_at > old_updated_at)

    def test_to_dict(self):
        """Test if to_dict method returns the correct dictionary"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertIsInstance(model_dict, dict)

        def test_str_method(self):
            """Test the __str__ method"""
            string = str(self.model)
            self.assertIn(f"[{self.model.__class__.__name__}] ({self.model.id})", string)