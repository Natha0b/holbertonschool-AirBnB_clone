#!/usr/bin/python3
'''test case'''
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''test case the amenity'''

    def test_create_amenity(self):
        '''checks if the instance has the required attributes.'''
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_attributes(self):
        '''checks if the name attribute
        is correctly set to an empty string.'''
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))

    def test_amenity_name(self):
        '''checks if the state_id attribute
        is correctly set to an empty string.'''
        amenity = Amenity()
        self.assertEqual(amenity.name, '')


if __name__ == '__main__':
    unittest.main()
