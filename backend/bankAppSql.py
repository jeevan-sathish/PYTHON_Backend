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


def createAcc():
    name = str(input("enter you name for bank account:")).strip()
    balance =int(input("enter 500 for minimum balance:"))
    query="select * from bank WHERE name =%s"
    val=(name,)
    cursor.execute(query,val)
    names=cursor.fetchone()
    if(names):
        print("user alreday exist enter diff name:")
    else:
        query="INSERT INTO bank(name,balance) VALUES(%s,%s)"
        val=(name,balance)
        cursor.execute(query,val)
        conn.commit()
        print("account created succesfull✅")
        query="select * from bank where name =%s"
        val=(name,)
        cursor.execute(query,val)
        acc=cursor.fetchone()
        print(acc[0])

def balanceEnq():
    name=str(input("enter you name as per bank :")).strip()
    query="select balance from bank where name =%s"
    val=(name,)
    cursor.execute(query,val)
    row =cursor.fetchone()
    if(row[0]):
        print("your current bank balance is :", row[0])
    else:
        print("user cannot be found ,create an account")
        
        

def depositeAmount():
    name=str(input("enter you name as per bank:")).strip()
    query="select name from bank where name =%s"
    val =(name,)
    cursor.execute(query,val)
    row =cursor.fetchone()
    if row is not None:
        amount=int(input("enter the deposite amount: "))
        query="update bank set balance = balance + %s where name =%s"
        val =(amount,name)
        cursor.execute(query,val)
        conn.commit()
        bal="select balance from bank where name =%s"
        v=(name,)
        cursor.execute(bal,v)
        balance_amount= cursor.fetchone()
        print("amount deposited succesfully, your current balance is :",balance_amount[0])
    else:
        print("user cannot be found ,create new account")
        createAcc()



def withdrawAmount():
    name=str(input("enter you name as per bank:")).strip()
    query="select name from bank where name =%s"
    val =(name,)
    cursor.execute(query,val)
    row =cursor.fetchone()
    if row is not None:
        amount=int(input("enter the withdraw amount: "))
        query="update bank set balance = balance - %s where name =%s"
        val =(amount,name)
        cursor.execute(query,val)
        conn.commit()
        bal="select balance from bank where name =%s"
        v=(name,)
        cursor.execute(bal,v)
        balance_amount= cursor.fetchone()
        print("amount withdrawal is  succesfully, your current balance is :",balance_amount[0])
    else:
        print("user cannot be found ,create new account")
        createAcc()



run =True
while(run):
    print('''
          select the operations you want:
          1.createAcount()
          2.Balance Enquiry()
          3.Deposit Amount()
          4.Withdraw Amount()
          0.exit
          ''')
    opn=int(input("enter the operation number 0-4:"))
    if(opn==1):
        createAcc()
    elif(opn==2):
       balanceEnq()
    elif(opn==3):
       depositeAmount()
    elif(opn==4):
        withdrawAmount()
    elif(opn==0):
        run=False
        print("Program exited successfully ✅")
    else:
        print("select the right operation number😡")
        

cursor.close()
conn.close()