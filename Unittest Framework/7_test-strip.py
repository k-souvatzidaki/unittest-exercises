import unittest
 
# run: python -m unittest 7_test-strip.py
class TestLstripMethod(unittest.TestCase):
 
    def test_lstrip_newline(self):
        self.assertEqual('\na,b\n'.lstrip(), 'a,b\n')
 
    def test_lstrip_tab(self):
        self.assertEqual('\ta,b\t'.lstrip(), 'a,b\t')
 
 
class TestStripMethod(unittest.TestCase):
 
    def test_strip_newline(self):
        self.assertEqual('\na,b\n'.strip(), 'a,b')
 
    def test_strip_spaces(self):
        self.assertEqual('     a,b '.strip(), 'a,b')
        self.assertEqual('     a  ,b '.strip(), 'a,b') # fail
 
 
class TestRstripMethod(unittest.TestCase):
 
    def test_rstrip_newline(self):
        self.assertEqual('\na,b\n'.rstrip(), '\na,b')
 
    def test_rstrip_tab(self):
        self.assertEqual('\ta,b\t'.rstrip(), '\ta,b')