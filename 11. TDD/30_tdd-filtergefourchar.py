import unittest

def filter_ge_four_char(words):
    return [x for x in words if len(x) >= 4] if len(words) !=0 else []


class TestFilterGeFourChar(unittest.TestCase):

    def test_filter_ge_four_char_with_one_item(self):
        msg = 'Correct the implementation of the filter_ge_four_char() function.'
        actual = filter_ge_four_char(['sql', 'r', 'java'])
        expected = ['java']
        self.assertEqual(actual, expected, msg)

    def test_filter_ge_four_char_with_two_item(self):
        msg = 'Correct the implementation of the filter_ge_four_char() function.'
        actual = filter_ge_four_char(['sql', 'r', 'python', 'java'])
        expected = ['python', 'java']
        self.assertEqual(actual, expected, msg)

    def test_filter_ge_four_char_should_be_empty(self):
        msg = 'Correct the implementation of the filter_ge_four_char() function.'
        actual = filter_ge_four_char([])
        expected = []
        self.assertEqual(actual, expected, msg)