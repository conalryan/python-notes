#!/usr/bin/env python

import unittest
from unittest.mock import Mock

"""
Return Values
    Create mock function with specified return value
    Use return_value param to Mock()
    You can have a mocked function or method return a specified value via the return_value parameter
"""
RETURN_VALUE = 99

# dependency to be mocked -- not used in test
# def ham():
#     return 42
# Create a mock function that returns 99; this simulates the real-life ham() function
ham = Mock(return_value=RETURN_VALUE)


# System under test
class Spam():
    def __init__(self):
        # Call mock function and get return value (Spam() does not know that it's not the "real" ham())
        self._value = ham()

    # Property to return value returned by ham()
    @property
    def value(self):
        return self._value


# Test case for Spam
class TestSpam(unittest.TestCase):

    def test_whatever(self):
        # Call Spam(), which in turn calls ham
        spam = Spam()
        # Check that spam.value (which was returned by ham()) is equal to the correct value
        self.assertEqual(RETURN_VALUE, spam.value, "value is not {}".format(RETURN_VALUE))


if __name__ == '__main__':
    unittest.main()

