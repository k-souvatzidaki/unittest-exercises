import unittest

def factorial(n):
    i = 1
    for x in range(1,n+1):
        i*=x
    return i

# or 

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        msg = 'Correct the implementation of factorial() function.'
        self.assertEqual(factorial(0), 1, msg)
        self.assertEqual(factorial(1), 1, msg)
        self.assertEqual(factorial(2), 2, msg)
        self.assertEqual(factorial(3), 6, msg)
        self.assertEqual(factorial(6), 720, msg)