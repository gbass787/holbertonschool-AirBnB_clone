#!/usr/bin/python3
'''unittests BaseModel class found in models/base_model.py'''

import os
import unittest
from time import sleep
import models
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    '''unittests for BaseModel class, testing: __init__, __str__,
    to_dict, attributes, and save methods from class.
    '''
    def test_id(self):
        '''Testing id attribute from BaseModel to make sure it's
        assigning a string.
        '''
        test_obj = BaseModel()
        self.assertEqual(type(test_obj.id), str)

    def test_created_at(self):
        '''Testing the created_at attribute from BaseModel to make sure
        it's assigning a datetime obj.
        '''
        test_obj = BaseModel()
        self.assertEqual(type(test_obj.created_at), datetime)

    def test_str(self):
        '''Testing the __str__ method of BaseModel, making sure all the attrs
        that it's supposed to include in the return string are there.
        '''
        test_obj = BaseModel()
        test_obj.id = "1"
        test_obj_str = test_obj.__str__()
        self.assertIn("[BaseModel]", test_obj_str)
        self.assertIn("1", test_obj_str)
        self.assertIn("'created_at'", test_obj_str)
        self.assertIn("'updated_at'", test_obj_str)

    def test_save_0(self):
        '''Testing the save method from BaseModel class by creating an
        object, then calling the save() method on it, and seeing if the
        second date is more recent than then older one.
        '''
        test_obj = BaseModel()
        created = test_obj.updated_at
        sleep(2)
        test_obj.save()
        updated = test_obj.updated_at
        self.assertLess(created, updated)

    def test_save_1(self):
        '''Testing the save method from BaseModel class by creating
        an object, then making the program wait 1 second before calling
        the save method from BaseModel and then comparing the created_at
        attr with the updated_at attr to make sure they are different
        '''
        test_obj = BaseModel()
        time_created = test_obj.created_at
        sleep(2)
        test_obj.save()
        time_updated = test_obj.updated_at
        self.assertNotEqual(time_created, time_updated)

    def test_to_dict(self):
        '''Testing the to_dict method by creating an object,
        initializing attributes to the values we  want, creating a
        dictionary that represents that to_dict called on the object
        that is supposed to return, and then calling to_dict
        method to see if it matches
        '''
        date = datetime.now()
        test_obj = BaseModel()
        test_obj.id = "1"
        test_obj.created_at = date
        test_obj.updated_at = date
        test_dict = {
                'id': '1',
                '__class__': 'BaseModel',
                'created_at': date.isoformat(),
                'updated_at': date.isoformat(),
                }
        self.assertDictEqual(test_obj.to_dict(), test_dict)

    def test_save(self):
        '''Testing save'''
        test_obj = BaseModel()
        created = test_obj.updated_at
        sleep(2)
        test_obj.save()
        updated = test_obj.updated_at
        self.assertLess(created, updated)

    def test_save5(self):
        '''Testing the save method'''
        test_obj = BaseModel()
        test_obj2 = FileStorage()
        models.storage.new(test_obj)
        models.storage.save()
        file_string = ""
        with open("file.json", 'r+') as jfile:
                file_string = jfile.read()
                self.assertIn("BaseModel.", file_string)

    def test_save8(self):
        '''testing save method'''
        obj = BaseModel()
        time1 = obj.updated_at
        obj.name = "Holby"
        obj.age = 1
        obj.save()
        time2 = obj.updated_at
        dict_obj = storage.all()
        obj_ref = storage.all().get("BaseModel.{}".format(obj.id))
        self.assertNotEqual(time1, time2)
        self.assertEqual(obj.id, obj_ref.id)
        self.assertEqual(obj.name, obj_ref.name)
        self.assertEqual(obj.age, obj_ref.age)
        self.assertTrue(os.path.exists('file.json'))

    def test_save_updates_file(self):
        test_model = BaseModel()
        test_model.save()
        tmid = "BaseModel." + test_model.id
        with open("file.json", "r") as jfile:
            self.assertIn(tmid, jfile.read())

if __name__ == '__main__':
        unittest.main()
