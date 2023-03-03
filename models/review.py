#!/usr/bin/python
'''class for update date'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''string - empty string'''
    place_id = str()
    user_id = str()
    text = str()
