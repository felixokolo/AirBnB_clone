#!/usr/bin/python
"""File storage engine"""
import json
from models.base_model import BaseModel

class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path (str): path to the JSON file (ex: file.json)
        __objects (dict): empty but will store all
        objects by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """returns the dictionary __objects"""
        return self.__objects


    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[type(obj).__name__ + "." + obj.id] = obj


    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dic = {k : v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(dic, f)
 
 
    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r") as f:
                dic = json.load(f)
                for k, v in dic.items():
                    FileStorage.__objects[k] = eval(k.split('.')[0])(**v)
        except Exception as e:
            pass
        
 