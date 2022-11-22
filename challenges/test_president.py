#!/usr/bin/env python

import unittest
from president import President
from datetime import datetime, date

"""
Create a unit test for the President class you created earlier. 
Suggestions for tests:
    What happens when an out-of-range term number is given
    President 1’s first name is "George"
    Date fields return an object of type datetime.date
"""
class TestPresident(unittest.TestCase):

    def test_raises_error(self):
        with self.assertRaises(ValueError):
            p = President(-1)

    def test_first_name_is_george(self):
        p = President(1)
        self.assertEqual(p.first_name, "George")

    def test_date_fields_are_datetime(self):
        p = President(1)
        self.assertIsInstance(p.birth_date, date)

if __name__ == '__main__':
    # Built in test runner .main()
    # When this script is run, it will execute the default text-based test runner
    unittest.main()