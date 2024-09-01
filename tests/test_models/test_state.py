#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_is_subclass(self):
        """Test that State is a subclass of BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_class_attributes(self):
        """Test default values for State class attributes."""
        state = State()
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()
