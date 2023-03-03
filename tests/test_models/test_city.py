#!/usr/bin/python3
'''test case'''
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    '''test case the City'''

    def test_create_city(self):
        '''checks if an instance can be created'''
        city = City()
        self.assertIsInstance(city, City)

    def test_city_attributes(self):
        '''checks if the instance has the required attributes.'''
        city = City()
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertTrue(hasattr(city, 'state_id'))

    def test_city_name(self):
        '''checks if the name attribute
        is correctly set to an empty string.'''
        city = City()
        self.assertEqual(city.name, '')

    def test_city_state_id(self):
        '''checks if the state_id attribute
        is correctly set to an empty string.'''
        city = City()
        self.assertEqual(city.state_id, '')


if __name__ == '__main__':
    unittest.main()
