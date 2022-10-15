#!/usr/bin/python3
'''BaseModel Unittests'''
import unittest
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage
import datetime


class BaseModelTests(unittest.TestCase):
    '''unittests for our BaseModel class'''

    my_model = BaseModel()

    def testBaseModel1(self):
        '''testing values of attributes'''

        self.my_model.name = "Holby"
        self.my_model.my_number = 42
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, "Holby")
        self.assertEqual(self.my_model.my_number, 42)
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])

    def testSave(self):
        '''Checks to see if save method updates updated_at'''
        self.my_model.first_name = "Alpha"
        self.my_model.save()

        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

        first_dict = self.my_model.to_dict()

        self.my_model.first_name = "Omega"
        self.my_model.save()
        sec_dict = self.my_model.to_dict()

        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])

if __name__ == '__main__':
    unittest.main()
