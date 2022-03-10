import unittest

# run: python -m unittest 18_test-employee-class.py
class Employee:
    tax_rate = 0.17
    bonus_rate = 0.1

    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
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

    @classmethod
    def setUp(this):
        this.emp = Employee('John','Smith',40,80000)

    def test_email(self):
        self.assertEqual(self.emp.email, 'john.smith@mail.com')

    def test_email_after_changing_first_name(self):
        self.emp.first_name = 'Mike'
        self.assertEqual(self.emp.email, 'mike.smith@mail.com')

    def test_email_after_changing_last_name(self):
        self.emp.last_name = 'Doe'
        self.assertEqual(self.emp.email, 'john.doe@mail.com')

    def test_get_salary(self):
        self.assertEqual(self.emp.salary,80000)

    def test_apply_bonus(self):
        self.emp.apply_bonus()
        self.assertEqual(self.emp.salary,88000)

    def test_employee_has_email_property(self):
        self.assertTrue(hasattr(Employee,'email'))
        self.assertIsInstance(Employee.email,property)