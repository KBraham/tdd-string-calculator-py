
import unittest


def add(numbers):
    if not numbers:
        return 0

    numbers = numbers.replace("\n", ",")

    parts = numbers.split(",")
    parts = [int(x) for x in parts]

    total = sum(parts)

    return total

class TestStringMethods(unittest.TestCase):
    def test_GivenEmptyStringExpectResultNot(self):
        self.assertEqual(add(""), 0)


    def test_GivenNumberExpectEqualNumberReturn(self):
        self.assertEqual(add("1"), 1)

    def test_GivenCommaSeparatedNumbersExpectSumOfNumbers(self):
        self.assertEqual(add("1,2"), 3)


    def test_GivenMultipleSeparatedNumbersExpectSumOfAll(self):
        self.assertEqual(add("1,2,3,4"), 10)

    def test_GivenMultipleNumbersWithNewLineExpectSumOfAll(self):
        self.assertEqual(add("2\n3,4"), 9)