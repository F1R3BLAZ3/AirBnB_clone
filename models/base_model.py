#!/usr/bin/python3

import cmd
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if args:
            for values in args:
                print(values)

        if kwargs:
            # Remove '__class__' from kwargs to prevent it from becoming an attribute
            class_name = kwargs.pop('__class__', None)
            if class_name:
                self.__class__ = class_name

            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    # Convert string to datetime
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        
        else:
        # create or assign ID, created_at and updated_at (new instance)
         self.id = str(uuid4())
         self.created_at = datetime.now()
         self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
