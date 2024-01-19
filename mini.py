import mysql.connector as ms
db=ms.connect(host="localhost", user="root", password="root", database="student")
cr=db.cursor()

class Student:
  def __init__(self=0,rno=0,name=0,fname=0,mname=0,sem=0,year=0,course=0,branch=0):
    self.rno=rno
    self.name=name
    self.fname=fname
    self.mname=mname
    self.sem=sem
    self.year=year
    self.course=course
    self.branch=branch

  def Display(self):
    print("\t\t\t\t RGPV BHOPAL \t\t\t")
    print("Roll =", self.rno ,"\t\t\t\t\t Course=",self.course)
    print("Name=",self.name,"\t\t\t\t\t branch=",self.branch)
    print("F. Name=",self.fname,"\t\t\t\t Sem=",self.sem)
    print("M. Name=",self.mname,"\t\t\t\t Year=",self.year,end="\n\n")

class Marks:
  def __init__(self,math=0,ada=0,se=0,coa=0,os=0):
    self.math=math
    self.ada=ada
    self.se=se
    self.coa=coa
    self.os=os

  def Display(self):
    print("SubCode \t SubName\t     MaxMarks\t   \tMinMarks\t ObtMarks")
    print("  401       \t   Maths    \t       70      \t       27       \t  ", self.math)
    print("  401       \t     ADA     \t       70      \t       27       \t  ", self.ada)
    print("  401       \t soft. engg\t       70      \t       27       \t  ", self.se)
    print("  401       \t    COA      \t       70      \t       27       \t  ", self.coa)
    print("  401       \t oper. sys \t       70      \t       27       \t  ", self.os,end="\n\n")

class result(Marks):
  def __init__(self,math=0,ada=0,se=0,coa=0,os=0):
    Marks.__init__(self,math,ada,se,coa,os)

  def Result(self):
    tot1=2*(self.math+self.ada+self.se+self.coa+self.os)
    tot=tot1/7
    if self.math<27 or self.ada<27 or self.se<27 or self.coa<27 or self.os<27:
      print("Better luck next time....You are fail!!")
      print("------------------------------------------------------------------------------------------------------------")
    elif tot<=45:
      print("You are pass with third division....Need more effort!!")
      print("------------------------------------------------------------------------------------------------------------")
    elif tot<=65:
      print("You are pass with second division....Gooood!!")
      print("------------------------------------------------------------------------------------------------------------")
    elif tot<=100:
      print("CONGRATULATION!!...You are pass with first division")
      print("------------------------------------------------------------------------------------------------------------")

  def Display(self):
    Marks.Display(self)



class Marksheet(Student,result):
  def __init__(self,rno=0,name=0,fname=0,mname=0,sem=0,year=0,course=0,branch=0,math=0,ada=0,se=0,coa=0,os=0):
    Student.__init__(self,rno,name,fname,mname,sem,year,course,branch)
    #Marks.__init__(self,math,ada,se,coa,os)
    result.__init__(self,math,ada,se,coa,os)

  def Display(self):
    Student.Display(self) 
    result.Display(self)
    result.Result(self)


while True:
  print("""
press 1 for insert the data
press 2 show all marksheeet
press 3 for search marksheet by roll number
press 5 for search marksheet by semester
press 6 for search marksheet by year
press 0 for exit

""")
  n=input("Enter the choice: ")
  if n=="1":
    try:
      m=int(input("How many data you want to insert: "))
    except ValueError:
      print("Input should be integer")
      continue
    cr.execute('select rno from data')
    dt1=cr.fetchall()
    ls=[]
    for i in dt1:
      ls.append(i[0])
    for i in range(3):
      r=input("Enter the roll number: ")
      if i==2 and (r in ls):
        print("Time out")
      elif r in ls:
        print("Roll number is already exit...plz enter another roll number")
        continue
      else:
        break
    if r in ls:
      continue

    na=input("Enter your name: ")
    fn=input("Enter father name: ")
    mn=input("Enter mother name: ")
    for i in range(3):
      try:
        sm=int(input("Enter semester: "))
      except ValueError:
        if i==0 or i==1:
          print("plz enter semster in numbers")
          continue
        elif i==2:
          print("Time out")
      if i==2 and (sm<1 or sm>8):
        print("Time out:")
      elif sm<1 or sm>8:
        print("semster in between 1 to 8")
        continue
      else:
        break
    if sm<1 or sm>8:
      break
    elif sm==1 or sm==2:
      yr=1
    elif sm==3 or sm==4:
      yr=2
    elif sm==5 or sm==6:
      yr=3
    elif sm==7 or sm==8:
      yr=4
    else:
      continue

    crs=input("Enter the course: ")
    br=input("Enter the Branch: ")


    for i in range(3):
      try:
        mat=int(input("Enter the math marks: "))
      except ValueError:
        if i==0 or i==1:
          print("Marks should be an integer")
          continue
        elif i==2:
          print("Time out")
      if (mat<0 or mat>70) and i==2:
        print("Marks is between 0 to 70...Time out")
      elif mat<0 or mat>70:
        print("Marks should not eexceed 70 and not be less than 0..pls renter")
        continue
      else:
        break
   
    if mat>=0 and mat<=70:
      pass
    else:
      continue
    



    for i in range(3):
      try:
        ad=int(input("Enter the ADA marks: "))
      except ValueError:
        if i==0 or i==1:
          print("Marks should be an integer")
          continue
        elif i==2:
          print("Time out")
      if ad<0 or ad>70 and i==2:
        print("Time out")
      elif ad<0 or ad>70:
        print("Marks should not eexceed 70 and not be less than 0..pls renter")
        continue
      else:
        break


    if ad>=0 and ad<=70:
      pass
    else:
      continue
    
    for i in range(3):
      try:
        so=int(input("Enter the Software marks: "))
      except ValueError:
        if i==0 or i==1:
          print("Marks should be an integer")
          continue
        elif i==2:
          print("Time out")
      if so<0 or so>70 and i==2:
        print("Time out")
      elif so<0 or so>70:
        print("Marks should not eexceed 70 and not be less than 0..pls renter")
        continue
      else:
        break
    if so>=0 and so<=70:
      pass
    else:
      continue
    
    for i in range(3):
      try:
        cso=int(input("Enter the CSO marks: "))
      except ValueError:
        if i==0 or i==1:
          print("Marks should be an integer")
          continue
        elif i==2:
          print("Time out")
          break
      if i==2 and (cso<0 or cso>70):
        print("Time out")
      elif cso<0 or cso>70:
        print("Marks should not eexceed 70 and not be less than 0..pls renter")
        continue
      else:
        break
    if cso>=0 and cso<=70:
      pass
    else:
      continue

    for i in range(3):
      try:
        op=int(input("Enter the Operating marks: "))
      except ValueError:
        if i==0 or i==1:
          print("Marks should be an integer")
          continue
        elif i==2:
          print("Time out")
      if op<0 or op>70 and i==2:
        print("Time out")
      elif op<0 or op>70:
        print("Marks should not eexceed 70 and not be less than 0..pls renter")
        continue
      else:
        break
    if op>=0 and op<=70:
      pass
    else:
      continue
    print("Data insert succesfull")


    cr.execute('insert into data values("{}","{}","{}","{}",{},{},"{}","{}",{},{},{},{},{})'.format(r,na,fn,mn,sm,yr,crs,br,mat,ad,so,cso,op))
    db.commit()

  elif n=="2":
    cr.execute('select* from data')
    dt=cr.fetchall()
    #print(dt)
    for i in dt:
      ob=Marksheet(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12])
      ob.Display()

  elif n=="3":
    cr.execute('select* from data')
    dt2=cr.fetchall()
    n=input("Enter the roll no you want search: ")
    for i in dt2:
      if i[0]==n:
         ob=Marksheet(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12])
         ob.Display()

  elif n=="4":
    cr.execute('select* from data')
    dt2=cr.fetchall()
    n=input("Enter the name you want search: ")
    for i in dt2:
      if i[1]==n:
         ob=Marksheet(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12])
         ob.Display()
 


  elif n=="5":
    cr.execute('select* from data')
    dt2=cr.fetchall()
    for i in range(3):
      try:
        n=int(input("Enter the semester you want search: "))
        break
      except ValueError:
        if i==2:
          print("Time out")
        else:
          print("Semester should be in integer")
    for i in dt2:
      if i[4]==n:
         ob=Marksheet(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12])
         ob.Display() 

  elif n=="6":
    cr.execute('select* from data')
    dt2=cr.fetchall()
    for i in range(3):
      try:
        n=int(input("Enter the year you want search: "))
        break
      except ValueError:
        if i==2:
          print("Time out")
        else:
          print("Year should be in integer")
    for i in dt2:
      if i[4]==n:
         ob=Marksheet(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12])
         ob.Display() 

     

  elif n=="0":
    break
  
    
    
    




#t1=Marksheet(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
#t1.Display()

