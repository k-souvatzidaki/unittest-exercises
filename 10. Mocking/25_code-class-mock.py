import random
import unittest
from unittest.mock import patch

# run: python -m unittest 25_code-class-mock.py
def get_code():
    rand_int = random.randint(10, 19)
    return f'CX-{rand_int}'

class TestGetCode(unittest.TestCase):

    @patch('random.randint')
    def test_get_code_mock_should_return_30(self,method):
        method.return_value = 30
        self.assertEqual(get_code(), 'CX-30')
