#!/usr/bin/python3
"""Unit test for Amenity class"""

from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """Amenity test"""

    def test_variable(self):
        """ Test if variables exists in class """
        obj = Amenity()
        self.assertEqual(obj.name, "")

    if __name__ == "__main__":
        unittest.main()
