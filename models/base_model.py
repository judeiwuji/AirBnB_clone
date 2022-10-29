#!/usr/bin/python3
"""
module base_model: contains class BaseModel
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    base class for other classes
    """

    def __init__(self, *args, **kwargs):
        """initiallization
            if dict is passed to it, it loads the instance with the
            key/value pair of the dict, otherwise creates new instance
            with new values.
        """

        if len(kwargs) > 0:
            for i in kwargs:
                value = kwargs[i]
                if i == "created_at" or i == "updated_at":
                    date_format = '%Y-%m-%dT%H:%M:%S.%f'
                    value = datetime.strptime(kwargs[i], date_format)
                if i != "__class__":
                    setattr(self, i, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """returns the str  format"""

        message = "[{}] ({}) {}"
        return message.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """

        new_dict = {}
        for i in self.__dict__:
            value = self.__dict__[i]
            if value is not None:
                new_dict[i] = value
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = (self.created_at).isoformat()
        new_dict["updated_at"] = (self.updated_at).isoformat()
        return new_dict
