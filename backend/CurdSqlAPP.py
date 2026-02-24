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

def addData():
    name=str(input("enter the name:"))
    age=int(input("enter the age:"))
    query ="INSERT INTO students(name,age) VALUES(%s,%s)"
    values =(name,age)
    cursor.execute(query,values)
    conn.commit()
    print("data inserted succefully✅")
    retriveData()

def updateData():
    purpose =str(input("enter what to abdate AGE or NAME:"))
    if(purpose.lower()=="age"):
        id=int(input("enter the ID:"))
        age=int(input("enter the AGE:"))
        query="update students set age=%s where id=%s"
        values=(age,id)
        cursor.execute(query,values)
        conn.commit()
        print("Age updated succefully✅")
        retriveData()
    elif(purpose.lower()=="name"):
         id=int(input("enter the ID:"))
         name=str(input("enter the AGE:"))
         query="update students set name=%s where id=%s"
         values=(name,id)
         cursor.execute(query,values)
         conn.commit()
         print("Name updated succefully✅")
         retriveData()
    else:
        print("enter correct operation")

def deleteData():
     purpose =str(input("enter what to delete by ID,AGE or NAME:"))
     if(purpose.lower()=="age"):
        age=int(input("enter the AGE:"))
        query="delete from students where age=%s"
        values=(age,)
        cursor.execute(query,values)
        conn.commit()
        print("deleted succefully✅ by age ")
        retriveData()
     elif(purpose.lower()=="name"):
         name=str(input("enter the AGE:"))
         query="delete from students where name=%s"
         values=(name,)
         cursor.execute(query,values)
         conn.commit()
         print("deleted succefully✅ by Name")
         retriveData()
     elif(purpose.lower()=="id"):
         id=str(input("enter the ID:"))
         query="delete from students where id=%s"
         values=(id,)
         cursor.execute(query,values)
         conn.commit()
         print("deleted succefully✅ by ID")
         retriveData()
     else:
        print("enter correct operation")
    
def clearAllRows():
    query="TRUNCATE TABLE students"
    cursor.execute(query)
    conn.commit()
    print("All cleared😉")
    retriveData()

def retriveData():
    query="select * from students"
    cursor.execute(query)
    data = cursor.fetchall()
    print("data in database:")
    for d in data:
        print(d)


def searchDataBy():
    purpose = input("Enter what to search by ID, AGE or NAME: ")

    if purpose.lower() == "age":
        age = int(input("Enter the AGE: "))
        query = "SELECT * FROM students WHERE age = %s"
        values = (age,)

    elif purpose.lower() == "name":
        name = input("Enter the NAME: ")
        query = "SELECT * FROM students WHERE name = %s"
        values = (name,)

    elif purpose.lower() == "id":
        id = int(input("Enter the ID: "))
        query = "SELECT * FROM students WHERE id = %s"
        values = (id,)

    else:
        print("Enter correct operation ❌")
        return

    cursor.execute(query, values)
    data = cursor.fetchall()

    if data:
        print("Search successful ✅")
        for row in data:
            print(row)
    else:
        print("No record found ❌")
    

run =True
while(run):
    print('''
          select the operations you want:
          1.addData()
          2.updateData()
          3.deleteData()
          4.retriveData()
          5.searchDataBy()
          0.exit
          ''')
    opn=int(input("enter the operation number 0-5:"))
    if(opn==1):
        addData()
    elif(opn==2):
        updateData()
    elif(opn==3):
        deleteData()
    elif(opn==4):
        retriveData()
    elif(opn==5):
        searchDataBy()
    elif(opn==0):
        run=False
        print("Program exited successfully ✅")
    else:
        print("select the right operation number😡")
        

conn.commit()
cursor.close()
conn.close()