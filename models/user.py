#!/usr/bin/python
'''class for update date'''
from models.base_model import BaseModel


class User(BaseModel):
    '''ensure that the objects are properly initialized.'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    '''string - empty string'''
    email = str()
    password = str()
    first_name = str()
    last_name = str()
