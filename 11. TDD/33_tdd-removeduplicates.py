import unittest

def remove_duplicates(items):
    return list(set(items))


class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates_empty_list(self):
        msg = 'Correct the implementation of the remove_duplicates() function.'
        self.assertEqual(remove_duplicates([]), [], msg)

    def test_remove_duplicates_without_string(self):
        msg = 'Correct the implementation of the remove_duplicates() function.'
        self.assertEqual(remove_duplicates([3, 3, 1]), [1, 3], msg)

    def test_remove_duplicates_with_three_string(self):
        msg = 'Correct the implementation of the remove_duplicates() function.'
        actual = sorted(remove_duplicates(['c++', 'c', 'c']))
        expected = ['c', 'c++']
        self.assertEqual(actual, expected, msg)