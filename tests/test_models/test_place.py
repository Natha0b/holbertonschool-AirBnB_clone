#!/usr/bin/python3
'''test case'''
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    '''test case the place'''

    def test_place_creation(self):
        '''check the attributes of a particular class'''
        place = Place()
        self.assertIsInstance(place, Place)


if __name__ == '__main__':
    unittest.main()
