import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
)

cursor = conn.cursor()


def handle_user():
    name = input("Enter your name: ")

    query = "INSERT INTO users(name) VALUES (%s)"
    val = (name,)

    cursor.execute(query, val)
    conn.commit()

    print("User inserted")


def handle_products():
    pid = int(input("Enter product id: "))
    name = input("Enter product name: ")

    query = "INSERT INTO products(product_id,product_name) VALUES (%s,%s)"
    val = (pid, name)

    cursor.execute(query, val)
    conn.commit()

    print("Product inserted")


def handle_orders():
    uid = int(input("Enter user id: "))
    pid = int(input("Enter product id: "))

    # insert order
    query = "INSERT INTO orders(users_id, product_id) VALUES (%s,%s)"
    val = (uid, pid)

    cursor.execute(query, val)
    conn.commit()

    print("Order inserted")

    # show order details
    query = """
        SELECT users.name, products.product_name
        FROM users
        JOIN orders ON users.id = orders.users_id
        JOIN products ON products.product_id = orders.product_id
    """

    cursor.execute(query)

    result = cursor.fetchall()

    for row in result:
        print("User:", row[0], "| Product:", row[1])



handle_orders()

cursor.close()
conn.close()