#!/usr/bin/python3
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_create_place(self):
        place = Place()
        self.assertIsInstance(place, Place)
        
if __name__ == "__main__":
    unittest.main()
