import unittest

# run: python -m unittest 16_test-tax-function.py
def calculate_tax(amount, age, tax=17.0):
    tax_rate = tax / 100.0
    if age <= 18:
        return int(min(amount * tax_rate, 6000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 9000))

class TestCalculateTax(unittest.TestCase):

    def test_tax_with_eighteen_age(self):
        self.assertEqual(calculate_tax(60000,18), 6000)

    def test_tax_with_nineteen_age(self):
        self.assertEqual(calculate_tax(60000,19), 10200)

    def test_tax_with_sixty_five_age(self):
        self.assertEqual(calculate_tax(60000,65), 10200)

    def test_tax_with_sixty_six_age(self):
        self.assertEqual(calculate_tax(60000,66), 9000)