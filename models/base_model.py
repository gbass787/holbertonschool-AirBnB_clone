#!/usr/bin/python3
'''class BaseModel that defines all common attributes/methods for other classes'''

from datetime import datetime
import models
import uuid

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    '''BaseModel class'''
    def __init__(self, *args, **kwargs):
        '''Initializes BaseModel attributes'''
        fmt = DATE_FORMAT

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            del kwargs['__class__']
            kwargs["created_at"] = datetime.strptime(kwargs['created_at'], fmt)
            kwargs["updated_at"] = datetime.strptime(kwargs['updated_at'], fmt)
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        '''Returns str representation of the instance'''
        class_name = self.__class__.__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        '''Saves object to JSON file'''

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Returns dictionary of all attributes of the BaseModel instance'''

        todic = self.__dict__.copy()
        todic["__class__"] = self.__class__.__name__
        todic["created_at"] = self.created_at.isoformat()
        todic["updated_at"] = self.updated_at.isoformat()

        return todic
