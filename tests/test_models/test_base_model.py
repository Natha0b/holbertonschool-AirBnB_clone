#!/usr/bin/python3
'''structure for the creation and organization the test'''
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''test'''
    '''test save the models'''
    def setUp(self):
        self.obj = BaseModel()
        self.obj.id = "test_id"
        self.obj.created_at = datetime.now()
        self.obj.updated_at = datetime.now()

    def test_save_method(self):
        '''check if the attribute is updated.'''
        initial_updated_at = self.obj.updated_at
        self.obj.save()
        new_updated_at = self.obj.updated_at
        self.assertGreater(new_updated_at, initial_updated_at)

    def test_id(self):
        '''Check id'''
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertTrue(type(obj1.id) == str)
        self.assertTrue(type(obj2.id) == str)

    def test_created_at(self):
        '''Check correctly created_at'''
        obj = BaseModel()
        self.assertTrue(obj.created_at is not None)
        self.assertTrue(isinstance(obj.created_at, datetime))

    def test_to_dict(self):
        '''check the dict'''
        mydict = { "id": "test_id",
            "created_at": self.obj.created_at.isoformat(),
            "updated_at": self.obj.updated_at.isoformat(),
            "__class__": "BaseModel"
            }
        self.assertDictEqual(mydict, self.obj.to_dict())

    def test_str(self):
        """test str"""
        string = f"[{self.obj.__class__.__name__}] ({self.obj.id}) {self.obj.__dict__}"
        self.assertEqual(string, self.obj.__str__())


if __name__ == "__main__":
    unittest.main()
