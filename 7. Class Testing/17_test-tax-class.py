import unittest

# run: python -m unittest 17_test-tax-class.py
class SimpleTaxCalculator:

    def income_tax(self, income, first_thresh=17.0, second_thresh=32.0):
        first_rate = first_thresh / 100.0
        second_rate = second_thresh / 100.0
        threshold = 85528
        if income < threshold:
            return income * first_rate
        else:
            return threshold * first_rate + (income - threshold) * second_rate

    def vat_tax(self, net_price, tax=23.0):
        tax_rate = tax / 100.0
        return net_price * tax_rate

    def capital_gains_tax(self, profit, tax=19.0):
        tax_rate = tax / 100.0
        if profit > 0:
            return profit * tax_rate
        return 0


def setUpModule():
    global calc
    calc = SimpleTaxCalculator()

class TestIncomeTax(unittest.TestCase):

    def test_income_below_threshold(self):
        self.assertEqual(calc.income_tax(60000), 10200)

    def test_income_equal_threshold(self):
        self.assertEqual(calc.income_tax(85528), 14539.76)

    def test_income_above_threshold(self):
        self.assertEqual(calc.income_tax(100000), 19170.8)


class TestVatTax(unittest.TestCase):

    def test_vat_tax_with_default(self):
        self.assertEqual(calc.vat_tax(100), 23.0)

    def test_vat_tax_with_twenty_tax_rate(self):
        self.assertEqual(calc.vat_tax(100, 20.0), 20.0)


class TestCapitalGainsTax(unittest.TestCase):

    def test_positive_profit(self):
        self.assertEqual(calc.capital_gains_tax(1000), 190.0)

    def test_zero_profit(self):
        self.assertEqual(calc.capital_gains_tax(0), 0.0)

    def test_negative_profit(self):
        self.assertEqual(calc.capital_gains_tax(-1000), 0.0)

# class TestIncomeTax(unittest.TestCase):
    
#     @classmethod
#     def setUpClass(this):
#         this.calc = SimpleTaxCalculator()
        
#     def test_income_below_threshold(self):
#         self.assertEqual(self.calc.income_tax(60000),10200)
        
#     def test_income_equal_threshold(self):
#         self.assertEqual(self.calc.income_tax(85528),14539.76)
    
#     def test_income_above_threshold(self):
#         self.assertEqual(self.calc.income_tax(100000),19170.8)


# class TestVatTax(unittest.TestCase):
    
#     @classmethod
#     def setUpClass(this):
#         this.calc = SimpleTaxCalculator()
        
#     def test_vat_tax_with_default(self):
#         self.assertEqual(self.calc.vat_tax(100),23.0)

#     def test_vat_tax_with_twenty_tax_rate(self):
#         self.assertEqual(self.calc.vat_tax(100,20.0),20.0)


# class TestCapitalGainsTax(unittest.TestCase):
    
#     @classmethod
#     def setUpClass(this):
#         this.calc = SimpleTaxCalculator()

#     def test_positive_profit(self):
#         self.assertEqual(self.calc.capital_gains_tax(1000),190.0)

#     def test_zero_profit(self):
#         self.assertEqual(self.calc.capital_gains_tax(0),0.0)

#     def test_negative_profit(self):
#         self.assertEqual(self.calc.capital_gains_tax(-1000),0.0)