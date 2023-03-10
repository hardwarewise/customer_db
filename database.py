import sqlite3

CREATE_CUSTOMERS_TABLE = """
CREATE TABLE IF NOT EXISTS customers (
                            id INTEGER PRIMARY KEY,
                            customer_id INTEGER,
                            name TEXT,
                            surname TEXT,
                            phone_number TEXT,
                            email TEXT,
                            address TEXT,
                            photo_path TEXT
                            );"""

INSERT_CUSTOMERS = """ 
INSERT INTO customers (
            customer_id,
            name,
            surname,
            phone_number,
            email,
            address,
            photo_path
            ) VALUES ( ?, ?, ?, ?, ?, ?, ?);
            """

GET_ALL_CUSTOMERS = """SELECT * FROM customers;"""

DELETE_CUSTOMER = """DELETE FROM customers WHERE id = ?;"""

UPDATE_CUSTOMER = """ UPDATE customers SET
                      customer_id = ?,
                      name = ?, surname = ?,
                      phone_number = ?, email = ?,
                      address = ?,
                      photo_path = ?
                      WHERE id = ?"""

GET_CUSTOMERS_BY_ANY = """
        SELECT * FROM customers WHERE
            customer_id || name || surname || email || phone_number || address LIKE ?;"""


def connect():
    return sqlite3.connect('data.db')


def create_tables(connection):
    with connection:
        connection.execute(CREATE_CUSTOMERS_TABLE)


def add_customers(connection, customer_id, name, surname, phone_number, email, address, photo_path):
    with connection:
        connection.execute(INSERT_CUSTOMERS, (customer_id, name, surname, phone_number, email, address, photo_path))


def get_all_customers(connection):
    with connection:
        return connection.execute(GET_ALL_CUSTOMERS).fetchall()


def get_customers_by_any(connection, searchstr):
    with connection:
        return connection.execute(GET_CUSTOMERS_BY_ANY, ('%' + searchstr + '%',)).fetchall()


def delete_customer(connection, id):
    with connection:
        return connection.execute(DELETE_CUSTOMER, id)


def update_customer(connection, customer_id, name, surname, phone_number, email, address, photo_path, id):
    with connection:
        connection.execute(UPDATE_CUSTOMER, (customer_id, name, surname,
         phone_number, email, address, photo_path, id))
