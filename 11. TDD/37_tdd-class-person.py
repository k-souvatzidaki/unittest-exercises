import unittest

class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"Person(fname='{self.fname}', lname='{self.lname}')"


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person('John', 'Smith')

    def test_person_repr_method(self):
        msg = 'Correct the implementation of the __repr__() method.'
        actual = repr(self.person)
        expected = "Person(fname='John', lname='Smith')"
        self.assertEqual(actual, expected, msg)