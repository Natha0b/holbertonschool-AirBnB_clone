#!/usr/bin/python3
import json
import os.path


class FileStorage:
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        class_name = obj.__class__.__name__
        key = f"{class_name}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        dic = []
        for key, val in self.__objects.items():
            dic[key] = val.to_dict()
            with open(self.__file_path, 'w') as jsonfile:
                json.dump(dic, jsonfile)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                load =  json.load(f)
                for key, val in load.items():
                    suma = eval(val["__class__"](**val))
                    FileStorage.__objects[key] = suma
