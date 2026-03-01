import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()


conn = mysql.connector.connect(
    user=os.getenv("DB_USER"),
    host =os.getenv("DB_HOST"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
    
)

with conn.cursor as cursor:
    print("connection succesfull")