import unittest

# run: python -m unittest 11_assert-in-raises-isinstance.py
class StringListOnly(list):

    def append(self, string):
        if not isinstance(string, str):
            raise TypeError('Only object of type str can be added to the list.')
        super().append(string)


class TestStringListOnly(unittest.TestCase):

    def test_slo_is_instance(self):
        slo = StringListOnly()
        self.assertIsInstance(slo,StringListOnly)
        self.assertIsInstance(slo,list)

    def test_append_string(self):
        string = 'hello'
        stringlist = StringListOnly([])
        stringlist.append(string)
        self.assertIn(string,stringlist)

    def test_append_not_string_should_raise_error(self):
        list = [1,2,3]
        boolean = True
        stringlist = StringListOnly([])
        self.assertRaises(TypeError, stringlist.append, list)
        self.assertRaises(TypeError, stringlist.append, boolean)