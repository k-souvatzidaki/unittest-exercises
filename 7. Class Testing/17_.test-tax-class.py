import unittest

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


class TestIncomeTax(unittest.TestCase):
    
    @classmethod
    def setUpClass(this):
        this.calc = SimpleTaxCalculator()
        
    def test_income_below_threshold(self):
        self.assertEqual(self.calc.income_tax(60000),10200)
        
    def test_income_equal_threshold(self):
        self.assertEqual(self.calc.income_tax(85528),14539.76)
    
    def test_income_above_threshold(self):
        self.assertEqual(self.calc.income_tax(100000),19170.8)