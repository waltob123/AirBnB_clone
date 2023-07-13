#!/usr/bin/python3
'''base module'''


import uuid
from datetime import datetime


class BaseModel:
    '''
    A base class defining methods and attributes that will
    be shared among the other classes.
    '''

    def __init__(self, *args, **kwargs):
        '''
        Instantiates an object with an id, the date it was created
        and the date it was updated.
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if len(kwargs) != 0:
            for key in kwargs.keys():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.fromisoformat(kwargs[key])
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()

    def save(self):
        '''
        Updates the updated_at attribute with the current date and time.
        '''
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        '''
        This method returns a dictionary containing all keys/values
        of __dict__ of the instance.
        '''
        obj_dict = {}
        obj_dict.update(self.__dict__)
        obj_dict.update({'__class__': self.__class__.__name__})
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        '''
        Returns a string representation of the object
        '''
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
