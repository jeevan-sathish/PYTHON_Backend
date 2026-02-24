import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


conn =mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
)

cursor =conn.cursor()
print("connected successfully")

query ="select * from students "
cursor.execute(query)
rows =cursor.fetchall()
for r in rows:
    print(r)

conn.commit()




cursor.close()
conn.close()