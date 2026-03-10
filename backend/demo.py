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

if conn.is_connected():
    print("Connected successfully")
else:
    print("Not connected")

cursor = conn.cursor()

try:
    query = "SELECT * FROM bank"
    cursor.execute(query)

    rows = cursor.fetchall()

    for r in rows:
        print(r)

except Exception as e:
    print("Error occurred:", e)
    conn.rollback()   # only useful if transaction failed

finally:
    cursor.close()
    conn.close()