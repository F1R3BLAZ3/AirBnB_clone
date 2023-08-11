#!/usr/bin/python3

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
    __file_path = "file.json"
    __objects = {}

    @property
    def file_path(self):
        return self.__file_path
    
    @file_path.setter
    def file_path(self, value):
        self.__file_path = value

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
        # convert the values to a dictionary using our save_to_dict() method
            obj_dict[key] = obj.to_dict()
            # open the file path for writing (serialization)
        with open(FileStorage.__file_path, 'w') as file:                                                   
            # dump the serialized object into the file
            json.dump(obj_dict, file)
    
    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="UTF8") as file:
                obj_dict = json.load(file)
                for key, obj_data in obj_dict.items():
                    class_name = obj_data["__class__"]
                    if class_name in globals():
                        cls = globals().get(class_name)
                        if cls:
                            cls_obj = cls(**obj_data)
                            key = "{}.{}".format(cls_obj.__class__.__name__, cls_obj.id)
                            self.__objects[key] = cls_obj
        else:
            self.__objects = {}  # Reset __objects to an empty dictionary
