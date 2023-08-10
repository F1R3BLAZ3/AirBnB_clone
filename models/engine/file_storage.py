#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:
    __filePath = "file.json"
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
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        obj_dict = {}
        for key, obj in self.__objects.items():
        # convert the values to a dictionary using our save_to_dict() method
            obj_dict[key] = obj.to_dict()
            # open the file path for writing (serialization)
            with open(self.__file_path, 'w') as file:                                                   
            # dump the serialized object into the file
                json.dump(obj_dict, file)
    
    def reload(self):
        # dictionary to hold all our defined classes (user-defined)
        definedClasses = {'BaseModel':BaseModel}

        # Attempt to open the Json file in the filePath
        try:
            with open(self.__file_path, 'r') as file:
            # deserialize the JSON string in the file at the file path
                obj_dict = json.load(file)
                # Iterate over each obj's value in the deserialized dictionary
                for key, obj_data in obj_dict.items():
                    # get obj's class name from the '__class__' key
                    class_name = obj_data["__class__"]
                    # get the actual class object in the definedClasses dictionary
                    obj = definedClasses[class_name]
                    # Create a new class instance with the object's values as                                                                                                                                                                              
                    # its arguments
                    self.new(obj(**obj_data))
        # Catch  FileNotFoundError and ignore if theres no file to deserialize
        except FileNotFoundError:
            pass
