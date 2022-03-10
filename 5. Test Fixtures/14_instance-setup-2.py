import unittest

# run: python -m unittest 14_instance-setup-2.py
class Container:

    def __init__(self, category):
        self.category = category

    def __repr__(self):
        return f"Container(category='{self.category}')"


class TestContainer(unittest.TestCase):
    
    # these methods are run in alphabetical!! order when unittest is run
    @classmethod
    def setUp(this):
        print('a')
        this.container = Container('plastic')

    # OR
    # def setUp(self):
    #   self.container = container('plastic')

    @classmethod
    def tearDown(this):
        print('b')
        del this.container

    # OR
    # def tearDown(self):
    #   del self.container

    def test_init_method(self):
        # container = Container('plastic')
        msg = 'The container instance does not have a category attribute.'
        # self.assertTrue(hasattr(container, 'category'), msg)
        self.assertTrue(hasattr(self.container, 'category'), msg)
        # self.assertEqual(container.category, 'plastic')
        self.assertEqual(self.container.category, 'plastic')

    def test_repr_method(self):
        # container = Container('plastic')
        # self.assertEqual(repr(container), "Container(category='plastic')")
        self.assertEqual(repr(self.container), "Container(category='plastic')")