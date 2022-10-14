#!/usr/bin/python3
"""Unit test for Amenity class"""

from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """City test"""

    def test_variable(self):
        obj = City()
        self.assertEqual(obj.state_id, "")
        self.assertEqual(obj.name, "")

    if __name__ == "__main__":
        unittest.main()
