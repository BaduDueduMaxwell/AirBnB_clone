#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_class_attributes(self):
        """Test default values for City class attributes."""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == '__main__':
    unittest.main()
