import unittest

# run: python -m unittest 10_assert-is-instance.py
class Employee:
    tax_rate = 0.17
    bonus_rate = 0.10

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@mail.com'

    @property
    def tax(self):
        return round(self.salary * self.tax_rate, 2)

    def apply_bonus(self):
        self.salary = int(self.salary * (1 + self.bonus_rate))


class TestEmployee(unittest.TestCase):

    def test_has_email_attr(self):
        self.assertTrue(hasattr(Employee,'email'), 'The Employee class does not have an email attribute.')

    def test_has_email_property(self):
        self.assertIsInstance(Employee.email, property)

    def test_has_tax_attr(self):
        self.assertTrue(hasattr(Employee,'tax'), 'The Employee class does not have a tax attribute.')

    def test_has_apply_bonus(self):
        self.assertTrue(hasattr(Employee,'apply_bonus'), 'The Employee class does not have an apply_bonus attribute.')