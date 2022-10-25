#!/usr/bin/python3
"""
module base_model: contains class BaseModel
"""

import uuid
import datetime

class BaseModel:
    """
    base class for other classes
    """

    def __init__(self):
        """initiallization"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()


    def __str__(self):
        message = "[{}] ({}) {}"
        return message.format(self.__class__.__name__, self.id, self.__dict__)


    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        new_dict = {}
        for i in self.__dict__:
            new_dict[i] = self.__dict__[i]
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = (self.created_at).isoformat()
        new_dict["updated_at"] = (self.updated_at).isoformat()
        return new_dict

