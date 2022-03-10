import uuid
import unittest

class Product:
    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return f"Product(product_name='{self.product_name}', price={self.price})"

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]


class TestProduct(unittest.TestCase):

    def test_product_has_get_id_function_attribute(self):
        self.assertTrue(hasattr(Product,'get_id'))
        self.assertTrue(callable(Product.get_id))