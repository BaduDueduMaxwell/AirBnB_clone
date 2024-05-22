import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model.name = "Test Model"
        model.my_number = 123
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('name', model_dict)
        self.assertIn('my_number', model_dict)
        self.assertEqual(model_dict['name'], 'Test Model')
        self.assertEqual(model_dict['my_number'], 123)

    def test_init_from_dict(self):
        # Create a dictionary representation of a BaseModel instance
        model_dict = {
            'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
            'created_at': '2017-09-28T21:03:54.052298',
            'updated_at': '2017-09-28T21:03:54.052302',
            'name': 'My_First_Model',
            'my_number': 89,
            '__class__': 'BaseModel'
        }

        # Recreate a BaseModel instance from the dictionary representation
        recreated_model = BaseModel(**model_dict)

        # Assert that the recreated instance has the same attributes \
        # and values as the original dictionary
        self.assertEqual(recreated_model.id, \
                         '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        self.assertEqual(recreated_model.created_at.isoformat(), \
                         '2017-09-28T21:03:54.052298')
        self.assertEqual(recreated_model.updated_at.isoformat(), \
                         '2017-09-28T21:03:54.052302')
        self.assertEqual(recreated_model.name, 'My_First_Model')
        self.assertEqual(recreated_model.my_number, 89)

if __name__ == '__main__':
    unittest.main()
