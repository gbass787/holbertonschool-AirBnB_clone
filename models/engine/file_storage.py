#!/usr/bin/python3
'''Manages file storage for BaseModel'''

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    '''Class serializes instances to a JSON file and
    deserializes JSON file to instances'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary self.__objects.'''
        return self.__objects

    def new(self, obj):
        '''Add the obj to the __objects dictionary with the key'''
        key = "{}.".format(obj.__class__.__name__)
        key += "{}".format(obj.id)
        self.__objects[key] = obj

    def save(self):
        '''Serializes the __objects attribute to a JSON file,
        the path is stored in the attribute __file_path variable'''
        copy_objects_dict = {}

        for key, value in self.__objects.items():
            copy_objects_dict[key] = value.to_dict()

        with open(self.__file_path, 'w+') as j_file:
            json.dump(copy_objects_dict, j_file)

    def reload(self):
        '''Desrializes the JSON file to __objects. If the file path does not
        exists, no exceptions are raised.
        '''
        try:
            with open(self.__file_path, 'r+') as j_file:
                new_dict = json.load(j_file)
            for key, value in new_dict.items():
                classes = key.split(".")
                self.__objects[key] = eval(classes[0])(**value)

        except:
            pass
