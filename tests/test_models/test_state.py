#!/usr/bin/python3
import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_create_city(self):
        city = City()
        self.assertIsInstance(city, City)

if __name__ == "__main__":
    unittest.main()
