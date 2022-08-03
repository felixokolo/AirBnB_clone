#!/usr/bin/python
"""File storage engine"""

class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path (str): path to the JSON file (ex: file.json)
        __objects (dict): empty but will store all
        objects by <class name>.id
    """

    __file_path = "file.json"
    __ojects = {}


    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects


    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.id] = obj
