#!/usr/bin/python3
'''test case'''
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    '''test case the place'''

    def setUp(self):
        '''checks if an instance can be created'''
        self.place = Place()

    def test_instance_creation(self):
        '''checks if the instance of the State
        class has the required attributes.'''
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        '''checks if the name attribute
        is correctly set to an empty string.'''
        self.assertEqual(self.place.city_id, str())
        self.assertEqual(self.place.user_id, str())
        self.assertEqual(self.place.name, str())
        self.assertEqual(self.place.description, str())
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
