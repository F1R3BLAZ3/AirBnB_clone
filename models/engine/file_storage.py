#!/usr/bin/python3

"""
This module defines the FileStorage class, which manages the serialization and
deserialization of objects to/from a JSON file. It provides methods to store
and retrieve objects in/from the file.
"""

import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Manages the serialization and deserialization of objects to/from
    a JSON file.

    This class provides methods to store and retrieve objects in/from the file.
    """

    __file_path = "file.json"  # Default file path
    __objects = {}  # Dictionary to store objects

    def all(self):
        """Returns the dictionary of objects."""
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary.

        Args:
            obj (BaseModel): The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes objects and saves them to the file.
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        # open the file path for writing (serialization)
        with open(self.__file_path, 'w') as file:
            # dump the serialized object into the file
            json.dump(obj_dict, file)
            file.close()

    def reload(self):
        """
        Deserializes objects and loads them from the file.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="UTF8") as file:
                obj_dict = json.load(file)
                for key, obj_data in obj_dict.items():
                    class_name = obj_data["__class__"]
                    if class_name in globals():
                        cls = globals().get(class_name)
                        if cls:
                            cls_obj = cls(**obj_data)
                            key = f"{cls_obj.__class__.__name__}.{cls_obj.id}"
                            self.__objects[key] = cls_obj
