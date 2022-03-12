import unittest

def map_longest(words):
    return max([len(x) for x in words]) if len(words) != 0 else 0

class TestMapLongest(unittest.TestCase):

    def test_map_longest_should_be_six(self):
        msg = 'Correct the implementation of the map_longest() function.'
        self.assertEqual(map_longest(['sql', 'r', 'python']), 6, msg)

    def test_map_longest_should_be_three(self):
        msg = 'Correct the implementation of the map_longest() function.'
        self.assertEqual(map_longest(['sql', 'r']), 3, msg)

    def test_map_longest_should_be_zero(self):
        msg = 'Correct the implementation of the map_longest() function.'
        self.assertEqual(map_longest([]), 0, msg)