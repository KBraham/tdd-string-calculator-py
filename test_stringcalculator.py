
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
        self.assertEqual(0, add(""))


    def test_GivenNumberExpectEqualNumberReturn(self):
        self.assertEqual(1, add("1"))

    def test_GivenCommaSeparatedNumbersExpectSumOfNumbers(self):
        self.assertEqual(3, add("1,2"))


    def test_GivenMultipleSeparatedNumbersExpectSumOfAll(self):
        self.assertEqual(10, add("1,2,3,4"))

    def test_GivenMultipleNumbersWithNewLineExpectSumOfAll(self):
        self.assertEqual(9, add("2\n3,4"))