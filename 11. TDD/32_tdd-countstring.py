import unittest

def count_string(items):
    return sum([1 for x in items if type(x)==str]) if len(items) != 0 else 0


class TestCountString(unittest.TestCase):

    def test_count_string_empty_list(self):
        msg = 'Correct the implementation of the count_string() function.'
        self.assertEqual(count_string([]), 0, msg)

    def test_count_string_without_string(self):
        msg = 'Correct the implementation of the count_string() function.'
        self.assertEqual(count_string([1, 2]), 0, msg)

    def test_count_string_with_three_string(self):
        msg = 'Correct the implementation of the count_string() function.'
        self.assertEqual(count_string(['c++', 3, 'c', 'java']), 3, msg)