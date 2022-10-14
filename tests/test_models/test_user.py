#!/usr/bin/python3
"""Unit test for Amenity class"""

from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """User test"""

    def test_variables(self):
        """ test if the variables exists inside the class """
        obj = User()
        self.assertEqual(obj.email, "")
        self.assertEqual(obj.password, "")
        self.assertEqual(obj.first_name, "")
        self.assertEqual(obj.last_name, "")

    if __name__ == "__main__":
        unittest.main()
