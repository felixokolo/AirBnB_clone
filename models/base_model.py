#!/usr/bin/python3
"""Base model package"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Base model class

    Attributes:
        id (str): unique id assigned when instance is created
        created_at (datetime): assign with the current datetime
        when an instance is created
        updated_at (datetime): assign with the current datetime
        when an instance is created and it will be updated every
        time you change your object
    """

    def __init__(self, *args, **kwargs):
        """Base class init

        Args:
            args (list): list of untagged arguments
            kwargs (dict): list of tagged arguments
        """
        if (kwargs == {}):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if (k == '__class__'):
                    continue
                if (k == 'updated_at' or k == 'created_at'):
                    new_time = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                    exec("self." + k + " = new_time")
                    continue
                exec("self." + k + " = v")

    def __str__(self):
        """prints dict of class"""
        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__))

    def save(self):
        """ updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        ret = self.__dict__.copy()
        ret['created_at'] = self.created_at.isoformat()
        ret['updated_at'] = self.updated_at.isoformat()
        ret['__class__'] = type(self).__name__
        return ret

# if __name__ == "__main__":
    # new = BaseModel()
    # print(new)
    # print(new.id)
    # print(new.created_at)
    # print(new.updated_at)
    # print(new.__str__)
