#!/usr/bin/python3
'class BaseModel that defines all common attributes/methods for other classes'

import uuid
from datetime import datetime
import models


class BaseModel:
    '''BaseModel Class'''
    def __init__(self, *args, **kwargs):
        '''Initializes BaseModel attributes'''
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    dt = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, dt)
                else:
                    if key != "__class__":
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        '''Returns str representation of the instance'''
        c_n = self.__class__.__name__
        return "[{}] ({}) {}".format(c_n, self.id, self.__dict__)

    def to_dict(self):
        '''Returns dictionary of all attributes of the BaseModel instance'''
        new_dict_copy = self.__dict__.copy()
        new_dict_copy['__class__'] = self.__class__.__name__
        new_dict_copy['created_at'] = self.created_at.isoformat()
        new_dict_copy['updated_at'] = self.updated_at.isoformat()
        return new_dict_copy

    def save(self):
        '''Saves object to JSON file'''
        self.updated_at = datetime.now()
        models.storage.save()
