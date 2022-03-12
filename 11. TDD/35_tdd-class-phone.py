import unittest

class Phone:

    brand = 'Apple'
    model = 'iPhone X'
    
class Laptop:

    def __init__(self,brand,model, price):
        if type(brand) == str:
            self.brand = brand
        else:
            raise TypeError
        self.model = model
        if price <= 0:
            raise ValueError
        if type(price) == int or type(price) == float:
            self.price = price
        else:
            raise TypeError
    

class TestPhone(unittest.TestCase):

    def test_brand_attr(self):
        msg = 'The brand attribute for the Phone class is missing.'
        self.assertTrue(hasattr(Phone, 'brand'), msg)

    def test_model_attr(self):
        msg = 'The model attribute for the Phone class is missing.'
        self.assertTrue(hasattr(Phone, 'model'), msg)

    def test_check_user_defined_class_attr(self):
        msg = 'Two Phone class attributes are not defined.'
        actual = len([attr for attr in dir(Phone) if not attr.startswith('_')])
        expected = 2
        self.assertEqual(actual, expected, msg)


class TestLaptop(unittest.TestCase):

    def test_laptop_incorrect_brand_should_raise_type_error(self):
        self.assertRaises(TypeError, Laptop, 200, 'Predator', 1000)
        self.assertRaises(TypeError, Laptop, True, 'Predator', 1000)

    def test_laptop_incorrect_price_should_raise_type_error(self):
        self.assertRaises(TypeError, Laptop, 'Acer', 'Predator', 'thousand')
        self.assertRaises(TypeError, Laptop, 'Acer', 'Predator', [2000])
        self.assertRaises(TypeError, Laptop, 'Acer', 'Predator', None)

    def test_laptop_incorrect_price_should_raise_value_error(self):
        self.assertRaises(ValueError, Laptop, 'Acer', 'Predator', -1000)
        self.assertRaises(ValueError, Laptop, 'Acer', 'Predator', 0)