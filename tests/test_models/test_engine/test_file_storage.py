#!/usr/bin/python3
"""Unit test for Amenity class"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCase):
    """Tests for File Storage"""

    def test_file_path(self):
        """ test for file path """
        obj = FileStorage()
        self.assertEqual(obj.__file_path, None)

    def test_objects(self):
        """ test for objects """
        FileStorage.__objects = {}

    def test_new(self):
        """ test the instance new """
        file = FileStorage()
        base = BaseModel()
        self.assertEqual(file.new(base), None)

    def test_save(self):
        """ test the instance save """
        obj = FileStorage()
        self.assertEqual(obj.save(), None)

    def test_reload(self):
        """ test the instance reload """
        obj = FileStorage()
        self.assertEqual(obj.reload(), None)

    def test_save_base(self):
        """ test the instance save of the BaseModel class """
        obj = BaseModel()
        self.assertEqual(obj.save(), None)

    def test_init_base(self):
        """ test init of BaseModel """
        obj = BaseModel()
        other = BaseModel()
        obj.name = "Juannito Perez"
        self.assertEqual(other.__init__(obj), None)

    if __name__ == "__main__":
        unittest.main()
