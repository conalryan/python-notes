#!/usr/bin/env python

# Test three functions from the random module:
import random
import unittest

"""
Unit Tests
    A test which asserts that an isolated piece of code (one function, method, or class) has some expected behavior.
    It's a way of making sure that code provides repeatable results.
    Three main components of a unit test:
        1. Unit tests - individual assertions that an expected condition has been met
        2. Test cases - collections of related unit tests
        3. Test runners - utilities to execute the tests in one or more test cases
    Unit tests should each test one aspect of your code, and each test should be independent of all other tests, including the order in which tests are run.

unittest module
    Provides automation for testing
    Test classes inherit form unittest.TestCase
    Provides base classes and tools for creating, running, and managing unit tests.

Create Test Case
    Inherit from unittest.TestCase
    Create one or more tests
    Add fixtures
    Individual test names must begin with "test" so they can be discovered by automated test runners.
    It's conventional to make test names verbose, so when test names are output, it's clear which tests are being run.
    Test case may contain fixtures, which are methods that contain shared code and data, so it doesn't have to be duplicated in many individual tests.

Fixtures
    Run before and after each test
    Factor out common code
    Predefined names: setUp() and tearDown()
    Class-level fixture: setUpClass and tearDownClass()
        Class-level fixtures must be decorated with @classmethod

Running Tests
    Run test script directly (unittest.main())
        If you have unittest.main() in the test script
        python test_wombats.py
    Use IDE's builtin test runner
    Use unittest
        python -m unittest test_wombats
        python -m unittest test_wombats.TestWombats
        python -m unittest test_wombats.TestWombats.test_wombat_shuffles_noisily

Skipping Tests
    Skip tests depending on circumstances
    Decorate with
        @unittest.skip(reason)
        @unittest.skipIf(true-condition, reason)
        @unittest.skipUnless(false-condition, reason)
    Create your own decorator function that returns unittest.skip() if the test should be skipped, and the function itself otherwise.

Automated Test Discovery
    Find tests (classes inheriting from unittest.TestCase)
    Create suites
    Run all tests
    To find all the tests in the specified foler and subfolders.
    Syntax
        python -m unittest discover
    Options
        -v, --verbose       verbose output
        -s, --start-directory   starting directory (defaults to .)
        -p, --pattern       pattern for test modules (defaults to test*.py)
        -t, --top-level-directory   top level of project (defaults to start directory)


Methods                     Assert that...
-------------------------------------------
assertAlmostEqual           Two expressions are equal [unequal] — difference between objects is less than the given delta (default zero).
assertNotAlmostEqual

assertDictContainsSubset    First dictionary is a superset of the second.

assertDictEqual             Two dictionaries have the same keys and values

assertEqual                 Two expressions are equal [unequal] as determined by the '==' operator.
assertNotEqual

assertGreater               The first expression is greater than the second

assertGreaterEqual          The first expression is greater than or equal to the second

assertIn                    The first expression is [not] a member of the second
assertNotIn

assertIs                    The first expression is [not] the same object as the second
assertIsNot

assertIsInstance            The first expression is [not] an instance of the second
assertNotIsInstance

assertIsNone                The expression is [not] None
assertIsNotNone

assertItemsEqual            The first expression and second expression have the same element counts (and the same elements, but not necessarily in the same order)

assertLess                  The first expression is less than the second

assertLessEqual             The first expression is less than or equal to the second

assertListEqual             The first list is equal to the second

assertMultiLineEqual        The first multi-line strings is equal to the second

assertRaises                The specified exception is raised when the specified callable is invoked

assertRegexpMatches         The expression matches [does not match] the specified regular expression (can be string or re instance)
assertNotRegexpMatches

assertSequenceEqual         The first ordered sequence (lists or tuples) is equal to the second

assertSetEqual              The first set is equal to the second

AssertTrue,                 The expression is True [False]
assert_ assertFalse

assertTupleEqual            The first tuple is equal to the second +2
"""


# TestCase objects contain one or more tests
class TestSequenceFunctions(unittest.TestCase):

    # setUpClass is called once at the beginning of the test case, before any test have run.
    # Any data created by setUpClass should not be modified by tests.
    @classmethod
    def setUpClass(cls):
        print("Starting all tests")

    # setUp is called before each test
    def setUp(self):
        print("Hello!")
        self.seq = list(range(10))

    # All tests must start with "test"
    def testshuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        # All test must assert some condition
        self.assertEqual(self.seq, list(range(10)))

    def testchoice(self):
        element = random.choice(self.seq)
        # There are many assertion types
        self.assertIn(element, self.seq)

    def testsample(self):
        self.assertRaises(ValueError, random.sample, self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertIn(element, self.seq)

    # tearDown is called after every test
    def tearDown(self):
        print("Goodbye!")

    # tearDownClass is called after all tests
    @classmethod
    def tearDownClass(cls):
        print("Ending all tests")


if __name__ == '__main__':
    # Built in test runner .main()
    # When this script is run, it will execute the default text-based test runner
    unittest.main()
