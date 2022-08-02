#!/usr/bin/python3
"""Base model package"""
import uuid
from datetime import datetime
class BaseModel:
    """Base model class
    """
    def __init__(self):
        """Base class init
        Attributes:
            id (str): unique id assigned when instance is created
            created_at (datetime): assign with the current datetime
            when an instance is created
            updated_at (datetime): assign with the current datetime
            when an instance is created and it will be updated every
            time you change your object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    #@property
    def __str__(self):
        """prints dict of class"""
        return ("[{}] ({}) {}".format(type(self).__name__,
            self.id, self.__dict__))

    def save(self):
        """ updates the public instance attribute updated_at with the
        current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        ret = self.__dict__
        ret['__class__'] = type(self).__name__
        return ret

if __name__ == "__main__":
    new = BaseModel()
    print(new)
    print(new.id)
    print(new.created_at)
    print(new.updated_at)
    print(new.__str__)
