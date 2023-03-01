#!/usr/bin/python3
'''class that  serializes and deserializes'''


import json
from os import path


class FileStorage:
    '''Private class attributes'''
    '''string'''
    __file_path = "file.json"
    '''dictionary '''
    __objects = {}

    '''Public instance methods'''
    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    '''Public instance methods'''
    def new(self, obj):
        '''sets in __objects the obj with key '''
        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj

    '''Public instance methods'''
    def save(self):
        '''serializes __objects to the JSON file '''
        dic = {}
        for key, val in self.__objects.items():
            dic[key] = val.to_dict()
        with open(self.__file_path, mode='w') as jsonfile:
            json.dump(dic, jsonfile)

    '''Public instance methods'''
    def reload(self):
        '''deserializes the JSON file to __objects '''
        from ..base_model import BaseModel

        try:
            with open(self.__file_path, mode='r') as file:
                file_objects = json.load(file)
            for key, value in file_objects:
                self.__objects[key] = eval(value["__class__"])(**value)
        except Exception:
            return
