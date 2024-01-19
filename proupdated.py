import mysql.connector as a
passwd=str(input("DATABASE PASSWORD:"))
con=a.connect(host="localhost",user="root",passwd="root")

c=con.cursor()
c.execute("show databases;")
dl=c.fetchall()
dl2=[]
for i in dl:
    dl2.append(i[0])
if 'bshop' in dl2:
    sql="use bshop;"
    c.execute(sql)
else:
    sql1="create database bshop;"
    c.execute(sql1)
    sql2="use bshop;"
    c.execute(sql2)
    sql3="""create table Gifts (Name varchar(50) , Cost price integer , selling price integer , Date varchar(20))"""
    c.execute(sql3)
    sql4="""create table Customer (Name varchar(50) , Gift varchar(50) , Payment integer , Date varchar(20) , Phone integer )"""
    c.execute(sql4)
    sql5="""create table Bills(Detail varchar(20) , Cost integer , Date varchar(20))"""
    c.execute(sql5)
    sql6="""create table Worker(Name varchar(50) , Work varchar(20) , Salary varchar(20))"""
    c.execute(sql6)

def signin():
    print("\n")
    print("-------------------->>>>> WELCOME TO BHOPAL GIFT SHOP <<<<<--------------------")
    print("\n")
    #p=input("System Password:")
    p="Hello123"
    if p=="Hello123":
        options()
    else:
        signin()

def options():
    print("""
                     1.    Add Gift
                     2.    Sell Gift
                     3.    Add Bill
                     4.    Add worker
                     5.    Display Gifts
                     6.    Display Payments
                     7.    Display Bills
                     8.    Display Workers

  """)
    choice = input("Select Option: ")
    while True:
      if(choice == '1'):
         AddGifts()
      elif(choice=='2'):
         SellGifts()
      elif(choice=='3'):
         AddBill()
      elif(choice=='4'):
         AddWorker()
      elif (choice=='5'):
         DisplayGifts()
      elif(choice=='6'):
         DisplayPayments()
      elif(choice=='7'):
         DisplayBills()
      elif (choice=='8'):
         DisplayWorker()
      else:
          print("Enter Again ............")
          options()


def AddGifts():
    n = input("Name: ")
    c = input("Cost price: ")
    b = input("Selling price: ")
    d = input("Date: ")
    data = (n,c,b,d)
    sql = 'insert into Gifts values(%s, %s, %s, %s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Inserted Successfully")
    options()

def SellGifts():
    n = input("Name:")
    g = input("Gift: ")
    py = int(input("Payment: "))
    d = input("Date: ")
    p = int(input("Phone: "))
    data = (n,g,py,d,p)
    sql = "insert into Customer values(%s, %s, %s, %s,%s)"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Inserted Successfully")
    options()

def AddBill():
    dt = input("Detail: ")
    c = int(input("Cost: "))
    d = input("Date: ")
    data = (dt,c,d)
    sql = 'insert into Bills values(%s, %s, %s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Inserted Successfully")
    options()
    
def AddWorker():
    n = input("Name:")
    w = input("Work: ")
    s = input("Salary: ")
    data = (n,w,s)
    sql = 'insert into Worker values(%s, %s, %s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data inserted Successfully")
    options()

def DisplayGifts():
    sql = 'select * from Gifts;'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    con.close()
    for i in d:
        print("Name:",i[0],"Cost price: ",i[1],"Selling price:",i[2],"Date: ",i[3])
        print("==========================================================================================")
    options()

def DisplayPayments():
    sql = 'select * from Customer;'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    con.close()
    for i in d:
         print("Name:",i[0],"Gift:",i[1],"Payment:",i[2],"Date:",i[3]," Phone:",i[4])
         print("==========================================================================================")
    options()

def DisplayBills():
    sql = 'select * from Bills;'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    con.close()
    for i in d:
        print("Detail: ",i[0]," Cost: ",i[1],"Date: ",i[2])
        print("==========================================================================================")
    options()

def DisplayWorker():
    sql = 'select * from Worker;'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    con.close()
    for i in d:
        print("Name: ",i[0]," Work: ",i[1], "Salary: ",i[2])
        print("==========================================================================================")
    options()

signin()    

        


         
 
