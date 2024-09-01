#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_class_attributes(self):
        """Test default values for Amenity class attributes."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

if __name__ == '__main__':
    unittest.main()
