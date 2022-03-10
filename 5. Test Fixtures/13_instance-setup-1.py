import unittest
import sys

class Container:

    def __init__(self):
        if sys.platform.startswith('win'):
            self.code = 'XC-win'
        else:
            self.code = f'XC-{sys.platform}'


class TestContainer(unittest.TestCase):

    # create and delete Container instance at the level of the entire testing class
    @classmethod
    def setUpClass(cls):
        cls.container = Container()

    @classmethod
    def tearDownClass(cls):
        del cls.container

    @unittest.skipUnless(sys.platform.startswith('win'), 'Requires Windows.')
    def test_requires_windows(self):
        c = Container()
        self.assertEqual(c.code, 'XC-win')

    @unittest.skipUnless(sys.platform.startswith('linux'), 'Requires Linux.')
    def test_requires_linux(self):
        c = Container()
        self.assertEqual(c.code, 'XC-linux')


# create and delete Container instance before and after testing
def setUpModule():
    global container
    container = Container()

def tearDownModule():
    global container
    del container