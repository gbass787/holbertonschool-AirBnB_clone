#!/usr/bin/python3
"""Unit test for Amenity class"""

from models.state import State
import unittest


class TestState(unittest.TestCase):
    """State test"""

    def test_variable(self):
        """ test if the variables exists inside the class """
        obj = State()
        self.assertEqual(obj.name, "")

    if __name__ == "__main__":
        unittest.main()
