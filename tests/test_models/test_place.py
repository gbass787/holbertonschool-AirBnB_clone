#!/usr/bin/python3
"""Unit test for Amenity class"""

from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Place test"""

    def test_variables(self):
        """ test if the variables exists inside the class """
        obj = Place()
        self.assertEqual(obj.city_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.description, "")
        self.assertEqual(obj.number_rooms, 0)
        self.assertEqual(obj.number_bathrooms, 0)
        self.assertEqual(obj.max_guest, 0)
        self.assertEqual(obj.price_by_night, 0)
        self.assertEqual(obj.latitude, 0.0)
        self.assertEqual(obj.longitude, 0.0)
        self.assertEqual(obj.amenity_ids, [])

    if __name__ == "__main__":
        unittest.main()
