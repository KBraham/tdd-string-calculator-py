
import unittest


def add(numbers):
        return 0

class TestStringMethods(unittest.TestCase):
    def test_GivenEmptyStringExpectResultNot(self):
        self.assertEqual(add(""), 0)
