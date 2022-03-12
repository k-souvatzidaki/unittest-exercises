from datetime import date
import unittest
from unittest.mock import patch

# message_generator.py
def get_today_name():
    return date.today().strftime('%A')

def get_message():
    return f'Hello {get_today_name()}!'


class TestGetMessage(unittest.TestCase):

    # @patch('message_generator.get_today_name')
    @patch('<module>.get_today_name') # TypeError: Need a valid target to patch. You supplied: 'get_today_name' (if no module given)
    def test_get_message_with_friday(self,function):
        function.return_value = 'Friday'
        self.assertEqual(get_message(),'Hello Friday!')

    @patch('message_generator.get_today_name')
    def test_get_message_with_monday(self,function):
        function.return_value = 'Monday'
        self.assertEqual(get_message(),'Hello Monday!')
