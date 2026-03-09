import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn =mysql.connector.connect(
    host =os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
)

cursor = conn.cursor()

if conn.is_connected():
    print("connected succesfully")
    
query =" SELECT users.name ,orders.product FROM users LEFT JOIN orders ON users.id = orders.user_id "
cursor.execute(query)
row =cursor.fetchall()

for r in row:
    print(r)


cursor.close()
conn.close()

