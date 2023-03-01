#!/usr/bin/python3
'''structure for the creation and organization the test'''
import unittest
from datetime import datetime
from models.base_model import BaseModel


class Test_base_models(unittest.TestCase):
    '''test'''
    '''test save the models'''
    def save_test_models(self):
        '''check if the attribute is updated.'''
        self.assertIsNone(self.obj.updated_at)
        self.obj.save()
        self.assertIsInstance(self.obj.updated_at, datetime)
        formerly = self.obj.updated_at
        self.obj.save()
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.assertNotEqual(self.obj.updated_at, formerly)

    '''test dictionary the models'''
    def test_to_dict(self):
        '''verifies that it returns the correct dictionary'''
        dict_create = self.obj.created_at()
        dict_updated = self.obj.updated_at
        self.assertDictEqual(dict_updated, dict_create)

    '''test str the class models'''
    def test__str__(self):
        '''verifies that the returned string is as expected.'''
        aux = self.obj.__class__.__name__
        string = f"[{aux}]({self.obj.id}){self.obj.__dict__}"
        self.assertEquals(string, self.obj.__str__())


if __name__ == "__main__":
    unittest.main()
