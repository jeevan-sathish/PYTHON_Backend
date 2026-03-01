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

cursor =conn.cursor(dictionary=True)

if conn.is_connected():
    print("connectuion succefull")
    try:
        def getData():
            query="SELECT * FROM employe"
            cursor.execute(query)
            rows =cursor.fetchall()
            for data in rows:
                print(data)
        
        def max_salary():
            query="SELECT MAX(salary) as Seniour_developer from employe "
            cursor.execute(query)
            data =cursor.fetchone()
            print("highest salary:", data["Seniour_developer"] )
            
        def insert_data():
            try:
                query="INSERT INTO employe(depID,name,dep,salary) VALUES(%s,%s,%s,%s)"
                depID=int(input("enter dep ID:"))
                name=str(input("enter your name:")).strip()
                depName=str(input("enter department name:")).strip()
                salary=float(input("enter your salary:"))
                val =(depID,name,depName,salary)
                cursor.execute(query,val)
                conn.commit()
                print(f"inserted data succesfull of {name} and {depName}")
                
            except Exception as e:
                conn.rollback()
                print("error in hadling:",str(e))
        
        def groupbyCallCount():
            
            try:
                query="SELECT dep, COUNT(*) as departMent_group from employe GROUP BY dep"
                cursor.execute(query)
                data=cursor.fetchall()
                for d in data:
                    print(d)
                    
            except Exception as e:
                print("error:",str(e))
        
    
                
                
    except Exception as e:
        print("error in handling",str(e))
    
else:
    print("failed")
    
cursor.close()
conn.close()