import uuid
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs,):
        # Initializes the class
        # self.my_number = my_number
        # self.name = name
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                self.created_at = datetime.strptime(kwargs['created_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
                self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
                self.id = kwargs['id']
        else:
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        # A representation of what the class should print out
        return "[{}] ({}) {}".format(str(self.__class__.__name__),
                                     str(self.id), str(self.__dict__))

    def save(self):
        # Updates the time when changes are made to the class
        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        # Copies self__dict__ and adds a  __class__ attribute
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': self.__class__.__name__,
                         'created_at': self.created_at.isoformat(),
                         'updated_at': self.updated_at.isoformat()})
        return new_dict
