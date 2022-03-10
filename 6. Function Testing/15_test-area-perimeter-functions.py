import unittest
import math

# run: python -m unittest 15_test-area-perimeter-functions.py
def area(radius):
    if not (isinstance(radius, (int, float))):
        raise TypeError('The radius must be of type int or float.')
    if not radius > 0:
        raise ValueError('The radius must be positive.')
    return math.pi * radius ** 2

def perimeter(radius):
    if not (isinstance(radius, (int, float))):
        raise TypeError('The radius must be of type int or float.')
    if not radius > 0:
        raise ValueError('The radius must be positive.')
    return 2 * math.pi * radius

class TestArea(unittest.TestCase):

    def test_circle_area_with_radius_one(self):
        rad = area(1)
        self.assertAlmostEqual(rad, 3.14159, 5)

    def test_circle_area_with_radius_three(self):
        rad = area(3)
        self.assertAlmostEqual(rad, 28.27433, 5)

    def test_area_incorrect_type_should_raise_type_error(self):
        self.assertRaises(TypeError, area, '4')
        self.assertRaises(TypeError, area, None)
 
    def test_area_incorrect_value_should_raise_value_error(self):
        self.assertRaises(ValueError, area, 0)
        self.assertRaises(ValueError, area, -3)

class TestPerimeter(unittest.TestCase):

    def test_circle_perimeter_with_radius_one(self):
        rad = perimeter(1)
        self.assertAlmostEqual(rad, 2*math.pi, 5)

    def test_circle_perimeter_with_radius_three(self):
        rad = perimeter(3)
        self.assertAlmostEqual(rad, 6*math.pi, 5)

    def test_perimeter_incorrect_type_should_raise_type_error(self):
        self.assertRaises(TypeError, perimeter, '4')
        self.assertRaises(TypeError, perimeter, None)
 
    def test_perimeter_incorrect_value_should_raise_value_error(self):
        self.assertRaises(ValueError, perimeter, 0)
        self.assertRaises(ValueError, perimeter, -3)