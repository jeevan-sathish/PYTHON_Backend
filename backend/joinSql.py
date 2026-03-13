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

def handle_user():
    name =str(input("enter your name:"))
    query = "insert into users(name) values(%s)"
    val =(name,)
    cursor.execute(query,val)
    conn.commit()

def handle_products()    


cursor.close()
conn.close()

