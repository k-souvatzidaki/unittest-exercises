import unittest
from sqlite3 import connect
from customers import CustomersDB


class TestCustomersDB(unittest.TestCase):

    def setUp(self):
        connection = connect(':memory:')
        cursor = connection.cursor()

        create_table_sql = """
            CREATE TABLE customers 
            ( 
                first_name TEXT, 
                last_name  TEXT, 
                email      TEXT, 
                phone      TEXT, 
                country    TEXT 
            );"""
        cursor.execute(create_table_sql)

        customers_data = [
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('John', 'Doe', 'john.doe@mail.com', '333', 'Canada'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        ]

        insert_sql = """
            INSERT INTO customers
            VALUES (?, ?, ?, ?, ?);"""
        cursor.executemany(insert_sql, customers_data)

        self.connection = connection

    def tearDown(self):
        self.connection.close()

    def test_add_customer(self):
        db = CustomersDB(self.connection)
        db.add_customer('Mike','Doe','mike.doe@mail.com','222','USA')
        cursor = self.connection.cursor()
        sql = """SELECT * FROM customers ORDER BY first_name,last_name;"""
        cursor.execute(sql)
        expected = (
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        )
        self.assertEqual(expected,tuple(cursor))

    def test_find_customers_by_first_name(self):
        db = CustomersDB(self.connection)
        result = tuple(db.find_customers_by_first_name('John'))
        expected = (
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA')
        )
        self.assertEqual(expected,result)

    def test_find_customers_by_country(self):
        db = CustomersDB(self.connection)
        result = tuple(db.find_customers_by_country('USA'))
        expected = (
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        )
        self.assertEqual(expected,result)
