#!/usr/bin/python3
'''test case'''
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    '''test case the User'''

    def test_attributes(self):
        '''check the attributes of a particular class'''
        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_create_user(self):
        '''check if an instance can be created'''
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
