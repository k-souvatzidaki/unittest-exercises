import unittest
from datetime import date
import sys

class Container:
    pass


class TestContainer(unittest.TestCase):

    def test_container(self):
        self.assertIsInstance(Container, type)

    @unittest.skip('The Container class requires implementation')
    def test_has_code_attribute(self):
        msg = 'The Container class does not have a code attribute.'
        self.assertTrue(hasattr(Container, 'code'), msg)

    @unittest.skipIf(date.today().day % 2 != 0, 'Skipping odd days.')
    def test_skipping_odd_days(self):
        c = Container()
        self.assertTrue(c.code.endswith('0'), 'Invalid code attribute.')

    @unittest.skipIf(date.today().day % 2 == 0, 'Skipping even days.')
    def test_skipping_even_days(self):
        c = Container()
        self.assertTrue(c.code.endswith('1'), 'Invalid code attribute.')

    @unittest.skipUnless(sys.platform.startswith('win'), 'Requires Windows.')
    def test_requires_windows(self):
        c = Container()
        self.assertEqual(c.code, 'XC-win')

    @unittest.skipUnless(sys.platform.startswith('linux'), 'Requires Linux.')
    def test_requires_linux(self):
        c = Container()
        self.assertEqual(c.code, 'XC-linux')