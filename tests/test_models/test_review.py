#!/usr/bin/python3
'''test case'''
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    '''test case the review'''

    def test_review_creation(self):
        '''check the attributes of a particular class'''
        review = review()
        self.assertIsInstance(review, review)


if __name__ == '__main__':
    unittest.main()
