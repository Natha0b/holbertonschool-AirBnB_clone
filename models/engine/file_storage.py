#!/usr/bin/python3
'''class that  serializes and deserializes'''


import json

class FileStorage:
    '''Private class attributes'''
    '''string'''
    __file_path = "file.json"
    '''dictionary '''
    __objects = dict()

    '''Public instance methods'''
    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    '''Public instance methods'''
    def new(self, obj):
        '''sets in __objects the obj with key '''
        class_name = obj.__class__.__name__
        key = f"{class_name}.{obj.id}"
        self.__objects[key] = obj

    '''Public instance methods'''
    def save(self):
        '''serializes __objects to the JSON file '''
        dic = {}
        for key, val in self.__objects.items():
            dic[key] = val.to_dict()
            with open(self.__file_path, 'w') as jsonfile:
                json.dump(dic, jsonfile)

    '''Public instance methods'''
    def reload(self):
        '''deserializes the JSON file to __objects '''
        try:
            with open(self.__file_path, mode='r') as file:
                file_objects = json.load(file).items()
                for key, value in file_objects:
                    eval(value["__class__"])(**value)
        except Exception:
            return
