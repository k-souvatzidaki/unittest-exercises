import unittest

# run: python -m unittest 5_assert-equal.py
class TestSplitMethod(unittest.TestCase):
    
    def test_split_by_default(self):
        self.assertEqual('Python Testing'.split(), ['Python', 'Testing']) # or assert actual == expected
 
    def test_split_by_comma(self):
        self.assertEqual('open,high,low,close'.split(','), ['open', 'high', 'low', 'close'])
 
    def test_split_by_hash(self):
        self.assertEqual('summer#time#vibes'.split('#'), ['summer', 'time', 'vibes']) 

class TestJoinMethod(unittest.TestCase):

    def test_join_with_space(self):
        self.assertEqual(' '.join(['Python', '3.8']), 'Python 3.8')
 
    def test_join_with_comma(self):
        self.assertEqual(','.join(['open', 'high', 'low', 'close']), 'open,high,low,close')
 
    def test_join_with_new_line_char(self):
        self.assertEqual('\n'.join(['open', 'high', 'low', 'close']), 'open\nhigh\nlow\nclose')