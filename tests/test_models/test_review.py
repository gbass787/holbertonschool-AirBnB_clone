#!/usr/bin/python3
"""Unit test for Amenity class"""
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """Review test"""

    def test_variables(self):
        """ test if the variables exists inside the class """
        obj = Review()
        self.assertEqual(obj.place_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.text, "")

    if __name__ == "__main__":
        unittest.main()
