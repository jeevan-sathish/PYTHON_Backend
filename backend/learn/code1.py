import mysql.connector
import os 
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user =os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
    
)

cursor =connection.cursor()
print("connected succesfull")

#transaction
try:
    
    query="INSERT INTO students(name,age) VALUES(%s,%s)"
    val=("sudeep",39)
    cursor.execute(query,val)
    
    
    query="INSERT INTO students(name,age) VALUES(%s,%s)"
    val=("sachin",27)
    cursor.execute(query,val)
    print("inserted data succeasfully")
    
    connection.commit()
    
except Exception as e:
   
    connection.rollback()
    print("error :" ,e)
    print("failed to add data ")


cursor.close()
connection.close()