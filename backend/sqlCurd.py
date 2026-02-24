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


def insertData(name,age):
    sql="INSERT INTO students(name,age) VALUES(%s, %s)"
    values=(name,age)
    print("data inserted")
    getDataAll()
    return cursor.execute(sql,values)
    

def updateData(d):
    update ="update students set age =%s where id = %s"
    val =(d,5)
    print("data updated")
    return cursor.execute(update,val)

def getDataAll():
    query ="select * from students"
    cursor.execute(query)
    rows =cursor.fetchall()
    for r in rows:
        print(r)

def getParticularData(id):
    query ="select name from students where id =%s"
    val =(id,)
    cursor.execute(query,val)
    data = cursor.fetchall()
    print("heres the data")
    for d in data:
        print(d)
        
def deleteData(id):
    query ="delete from students where id=%s"
    val =(id,)
    cursor.execute(query,val)
    print("data deleted")
    getDataAll()
    

# insertData("ajay",23)
# updateData(19)
# getParticularData(1)
deleteData(8)
conn.commit()




cursor.close()
conn.close()