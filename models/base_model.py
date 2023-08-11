#!/usr/bin/python3

"""
This module contains the BaseModel class, which serves as the base class for
object models. It provides common attributes and methods for managing instances
of various models, including ID assignment, time tracking, and instance
serialization.
"""

import cmd
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class for object models.

    This class provides common attributes and methods for managing instances
    of various models. It handles ID assignment, time tracking, and instance
    serialization.

    Attributes:
        id (str): A unique identifier for the instance.
        created_at (datetime): The timestamp when the instance was created.
        updated_at (datetime): The timestamp when the instance was last updated
    """

    def __init__(self, *args, **kwargs):
        # Import the storage module for handling instances
        from models import storage

        if args:
            # Handle arguments, if any
            for values in args:
                print(values)

        if kwargs:
            # Remove '__class__' from kwargs to prevent it from becoming
            # an attribute
            class_name = kwargs.pop('__class__', None)
            if class_name:
                # Dynamically set the class based on the '__class__' attribute
                cls = globals().get(class_name, None)
                if cls:
                    self.__class__ = cls

            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    # Convert string to datetime for time attributes
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)

        else:
            # For new instances, assign ID, created_at, and updated_at
            self.id = str(uuid4())  # Assign a unique identifier
            self.created_at = datetime.now()  # Set creation timestamp
            self.updated_at = datetime.now()  # Set update timestamp
            storage.new(self)  # Add instance to storage

    def __str__(self):
        """Returns a string representation of the instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the 'updated_at' attribute and saves the instance."""
        from models import storage
        self.updated_at = datetime.now()  # Update the update timestamp
        storage.save()  # Save changes to storage

    def to_dict(self):
        """Converts the instance to a dictionary representation."""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__  # Add class name
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
