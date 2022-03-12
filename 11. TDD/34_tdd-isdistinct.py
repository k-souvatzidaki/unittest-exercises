import unittest

def is_distinct(items):
    return len(items) == len(set(items))

class TestIsDistinct(unittest.TestCase):

    def test_is_distinct_empty_list(self):
        msg = 'Correct the implementation of the is_distinct() function.'
        self.assertEqual(is_distinct([]), True, msg)

    def test_is_distinct_with_numbers_should_return_false(self):
        msg = 'Correct the implementation of the is_distinct() function.'
        self.assertEqual(is_distinct([3, 3, 1]), False, msg)

    def test_is_distinct_with_numbers_should_return_true(self):
        msg = 'Correct the implementation of the is_distinct() function.'
        self.assertEqual(is_distinct([3, 2, 1]), True, msg)

    def test_is_distinct_with_strings(self):
        msg = 'Correct the implementation of the is_distinct() function.'
        self.assertEqual(is_distinct(['c++', 'c', 'r']), True, msg)