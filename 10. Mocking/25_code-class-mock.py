import random
import unittest
from datetime import date
from unittest.mock import patch

# codegenerator.py
def get_code():
    rand_int = random.randint(0, 9)
    return f'CX-{rand_int}'

def get_today_name():
    return date.today().strftime('%a')

def get_code_with_day():
    code = get_code()
    dayname = get_today_name().upper()
    return f'{code}-{dayname}'

class TestGetCode(unittest.TestCase):

    @patch('random.randint')
    def test_get_code_mock_should_return_30(self,method):
        method.return_value = 30
        self.assertEqual(get_code(), 'CX-30')

class TestGetCodeWithDay(unittest.TestCase):

    # @patch('random.randint')
    # @patch('code_generator.get_today_name')
    # !!! order of patches is important 
    @patch('code_generator.get_today_name')
    @patch('random.randint')
    def test_get_code_with_day_with_mocked_friday(self,method1,method2):
        method1.return_value = 30
        method2.return_value = 'FRI'
        self.assertEqual(get_code_with_day(), 'CX-30-FRI')

    @patch('code_generator.get_today_name')
    @patch('random.randint')
    def test_get_code_with_day_with_mocked_monday(self,method1,method2):
        method1.return_value = 20
        method2.return_value = 'MON'
        self.assertEqual(get_code_with_day(), 'CX-20-MON')
