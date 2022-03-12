import unittest

class Pet:

    def __init__(self, name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


class TestPet(unittest.TestCase):

    def test_pet_has_name_property(self):
        msg = 'The Pet class does not have a name attribute.'
        self.assertTrue(hasattr(Pet, 'name'), msg)
        self.assertIsInstance(Pet.name, property)

    def test_pet_has_age_property(self):
        msg = 'The Pet class does not have an age attribute.'
        self.assertTrue(hasattr(Pet, 'age'), msg)
        self.assertIsInstance(Pet.age, property)