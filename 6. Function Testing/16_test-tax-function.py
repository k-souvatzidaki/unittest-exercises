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


def income_tax(income, first_thresh=17.0, second_thresh=32.0):
    first_rate = first_thresh / 100.0
    second_rate = second_thresh / 100.0
    threshold = 85528
    if income < threshold:
        return income * first_rate
    else:
        return threshold * first_rate + (income - threshold) * second_rate


class TestCalculateTax(unittest.TestCase):

    def test_tax_with_eighteen_age(self):
        self.assertEqual(calculate_tax(60000,18), 6000)

    def test_tax_with_nineteen_age(self):
        self.assertEqual(calculate_tax(60000,19), 10200)

    def test_tax_with_sixty_five_age(self):
        self.assertEqual(calculate_tax(60000,65), 10200)

    def test_tax_with_sixty_six_age(self):
        self.assertEqual(calculate_tax(60000,66), 9000)

    def test_tax_twenty_percent_with_eighteen_age(self):
        self.assertEqual(calculate_tax(60000,18,20), 6000)

    def test_tax_twenty_percent_with_nineteen_age(self):
        self.assertEqual(calculate_tax(60000,19,20), 12000)

    def test_tax_twenty_percent_with_sixty_five_age(self):
        self.assertEqual(calculate_tax(60000,65,20), 12000)

    def test_tax_twenty_percent_with_sixty_six_age(self):
        self.assertEqual(calculate_tax(60000,66,20), 9000)


class TestIncomeTax(unittest.TestCase):
    
    def test_tax_below_threshold(self):
        self.assertEqual(income_tax(60000),10200)
        
    def test_tax_equal_threshold(self):
        self.assertEqual(income_tax(85528),14539.76)
    
    def test_tax_above_threshold(self):
        self.assertEqual(income_tax(100000),19170.8)