#!/usr/bin/python3
'''structure for the creation and organization the test'''
import unittest
from datetime import datetime


class Test_file_strorage(unittest.TestCase):
    def test_all (self):
        self.assertEqual(type(self.storage.all()), dict)


if __name__ == "__main__":
    unittest.main()



if __name__ == "__main__":
    unittest.main()
