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
else:
    print("not connected")
    
query =" SELECT * FROM bank "
cursor.execute(query)
row =cursor.fetchall()

for r in row:
    print(r)


cursor.close()
conn.close()

