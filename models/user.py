#!/usr/bin/python
'''class for update date'''
from models.base_model import BaseModel


class User(BaseModel):

    '''string - empty string'''
    email = str()
    password = str()
    first_name = str()
    last_name = str()
