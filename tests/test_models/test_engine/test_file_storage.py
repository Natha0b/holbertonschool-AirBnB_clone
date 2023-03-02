#!/usr/bin/python3
'''structure for the creation and organization the test'''
import unittest
import os
import json
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_file_strorage(unittest.TestCase):
    '''test case'''

    def setUp(self):
        '''rename file.json'''
        self.storage = FileStorage()
        try:
            os.remove(FileStorage._FileStorage__file_path, "newfile.json")
        except Exception:
            pass

    
    def tearDown(self):
        '''delete and rename the file'''
        try:
            os.remove(FileStorage._FileStorage__file_path, "newfile.json")
        except Exception:
            pass
        try:
            os.rename("newfile.json", FileStorage._FileStorage__file_path)
        except Exception:
            pass

    def test_all(self):
        '''test case the dictionary __objects'''
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        '''test case sets in __objects the obj with key'''
        my_instance = BaseModel()
        self.storage.new(my_instance)
        key = my_instance.__class__.__name__ + "." + my_instance.id
        self.assertIn(key, self.storage.all())

    def test_save(self):
        '''serializes __objects to the JSON file'''
        my_instance =  BaseModel()
        self.storage.new(my_instance)
        my_instance.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload(self):
        '''test deserializes the JSON file to __objects'''
        my_instance =  BaseModel()
        self.storage.new(my_instance)
        self.storage.save()
        self.storage._FileStorage__objects.clear()
        self.storage.reload()
        key = my_instance.__class__.__name__ + "." + my_instance.id
        self.assertIn(key, self.storage.all())





if __name__ == "__main__":
    unittest.main()
