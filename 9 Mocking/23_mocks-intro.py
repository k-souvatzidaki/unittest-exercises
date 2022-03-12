from unittest.mock import Mock
import random

# run: python -m unittest 23_mocks-intro.py
mock = Mock(name='first_mock')
print(mock)

techs = ['python', 'sql', 'java', 'aws', 'c++']
random.choice = Mock(return_value='aws')
print(random.choice())

print(random.choice.call_count)
random.choice()
print(random.choice.call_count)