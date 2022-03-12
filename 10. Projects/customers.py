class CustomersDB:

    def __init__(self, connection):
        self.connection = connection

    def add_customer(
        self,
        first_name,
        last_name,
        email,
        phone,
        country
    ):
        cursor = self.connection.cursor()
        sql = """
            INSERT INTO customers
            VALUES (:first_name, :last_name, :email, :phone, :country);"""
        cursor.execute(sql, locals())
        self.connection.commit()
        return cursor.lastrowid