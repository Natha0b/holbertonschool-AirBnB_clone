#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage

class BaseModel:
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
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        dic_now = dict()
        for (key, value) in (self.__dict__).items():
            dic_now["__clas"] = self.__class__.__name__
            if isinstance(value, datetime):
                dic_now[key] = value.isoformat()
            else:
                dic_now[key] = value
        return dic_now
