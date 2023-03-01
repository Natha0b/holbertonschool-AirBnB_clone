#!/usr/bin/python3
"""Import"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Define the class BaseModel"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != __class__.__name__:
                    setattr(self, key, value)
            a_format = "%Y-%m-%dT%H:%M:%S.%f"
            self.created_at = datetime.strptime(self.created_at, a_format)
            self.updated_at = datetime.strptime(self.updated_at, a_format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """returns the string defined in this method."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """public instance attribute with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        dic_now = dict()
        for (key, value) in (self.__dict__).items():
            dic_now["__class"] = self.__class__.__name__
            if isinstance(value, datetime):
                dic_now[key] = value.isoformat()
            else:
                dic_now[key] = value
        return dic_now
