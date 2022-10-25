#!/usr/bin/python3
"""
module base_model: contains class BaseModel
"""


import uuid
from datetime import datetime


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
        if kwargs is not None and kwargs != {}:
            for i in kwargs:
                if i == "created_at":
                    C_dt = datetime.strptime(kwargs[i], '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, i, C_dt)
                elif i == "updated_at":
                    U_dt = datetime.strptime(kwargs[i], '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, i, U_dt)
                else:
                    if i != "__class__":
                        setattr(self, i, kwargs[i])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

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
