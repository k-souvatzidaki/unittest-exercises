import unittest

def calc_tax(amount, tax_rate, age):
    if not isinstance(amount, (int, float)):
        raise TypeError('The amount value must be int or float type.')
    if not amount >= 0:
        raise ValueError('The amount value must be positive.')

    if not isinstance(tax_rate, float):
        raise TypeError('The tax_rate must be float.')
    if not 0 < tax_rate < 1:
        raise ValueError('The tax_rate must be between 0 and 1 (exclusive).')

    if not isinstance(age, int):
        raise TypeError('The age value must be int.')
    if not age > 0:
        raise ValueError('The age value must be positive.')

    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 8000))

class TestCalcTax(unittest.TestCase):

    # def test_calc_tax_twenty_percent_and_eighteen_age(self):
    #     self.assertEqual(calc_tax(60000,0.2,18), 5000)

    # def test_calc_tax_twenty_percent_and_nineteen_age(self):
    #     self.assertEqual(calc_tax(60000,0.2,19), 12000)

    # def test_calc_tax_twenty_percent_and_sixty_five_age(self):
    #     self.assertEqual(calc_tax(60000,0.2,65), 12000)

    # def test_calc_tax_twenty_percent_and_sixty_six_age(self):
    #     self.assertEqual(calc_tax(60000,0.2,66), 8000)

    def test_calc_tax(self):
        cases = [
            (60000,0.2,18, 5000), 
            (60000,0.2,19, 12000),
            (60000,0.2,65, 12000),
            (60000,0.2,66, 8000)
        ]
        for amount,tax_rate, age, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(calc_tax(amount,tax_rate,age),result)
