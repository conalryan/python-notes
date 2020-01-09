#!/usr/bin/env python

import unittest
from unittest.mock import Mock

"""
Mocking Data
    Simulate behavior of actual objects
    Replace expensive dependencies (time/resources)
    Use unittest.mock (formerly pymock)
    Stub
        Object that returns minimal information, and is also useful in testing
    Mock object is more elaborate (than a stub), with record/playback capability, assertions, and other features.
    Mock Objects
        Use unittest.mock.Mock
        Callable, so emulate functions or classes
        Return themselves by default
    MagicMock
        Object is like Mock, but also has all of the "magic" methods (str(), lent(), etc.) defined
"""

# dependency to be mocked -- not used in test
# def ham(n):
#     pass
# Create Mock object - it will be used as a function here, but can be used as anything
ham = Mock()


# system under test
class Spam():
    def __init__(self, param):
        # Call the mock "ham()" function - works like the real ham() function
        self._value = ham(param)


# Test case that will use the mick
class TestSpam(unittest.TestCase):

    def test_spam_calls_ham(self):
        # Spam constructor calls ham()
        spam = Spam(42)
        # Assert that ham was called with the correct argument
        ham.assert_called_once_with(42)


if __name__ == '__main__':
    unittest.main()

