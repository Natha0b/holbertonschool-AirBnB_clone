#!/usr/bin/python3
'''test case'''
import unittest
from models.state import State


class TestState(unittest.TestCase):
    '''test case the state'''

    def test_create_state(self):
        '''checks if an instance can be created'''
        state = State()
        self.assertIsInstance(state, State)

    def test_state_attributes(self):
        '''checks if the instance of the State
        class has the required attributes.'''
        state = State()
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))

    def test_state_name(self):
        '''checks if the name attribute
        is correctly set to an empty string.'''
        state =State()
        self.assertEqual(state.name, '')


if __name__ == '__main__':
    unittest.main()
