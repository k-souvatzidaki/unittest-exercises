import unittest

class Vector:

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __len__(self):
        return len(self.components)

class TestVector(unittest.TestCase):

    def setUp(self):
        self.v = Vector(-3, 4, 2)
        self.w = Vector(1, -3)

    def test_vector_repr_method(self):
        msg = 'Correct the implementation of the __repr__() method.'
        self.assertEqual(repr(self.v), "Vector(-3, 4, 2)", msg)
        self.assertEqual(repr(self.w), "Vector(1, -3)", msg)

    def test_vector_len_method(self):
        msg = 'Correct the implementation of the __len__() method.'
        self.assertEqual(len(self.v), 3, msg)
        self.assertEqual(len(self.w), 2, msg)