#!/usr/bin/python3
'''test case'''
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    '''test case the review'''

    def setUp(self):
        '''checks if an instance can be created'''
        self.review = Review()

    def test_instance_creation(self):
        '''checks if the instance of the State
        class has the required attributes.'''
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        '''checks if the name attribute
        is correctly set to an empty string.'''
        self.assertEqual(self.review.place_id, str())
        self.assertEqual(self.review.user_id, str())
        self.assertEqual(self.review.text, str())


if __name__ == '__main__':
    unittest.main()
