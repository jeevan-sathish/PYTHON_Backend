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
print("connect successfully")


query ="INSERT INTO customer(name,acc1) VALUES(%s,%s)"
values=("sumanth",27000)
cursor.execute(query,values)
conn.commit()
print("inserted")

query="select acc1 from customer where id=%s "
val=(2,)
cursor.execute(query,val)
bal =cursor.fetchone()
print(bal[0])

if(bal[0]>=30000):
    print("oo u are rich")
else:
    print("poor")



cursor.close()
conn.close()