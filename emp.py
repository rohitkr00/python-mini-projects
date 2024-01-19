import mysql.connector as ms
db=ms.connect(host="localhost", user="root", password="root", database="emp")
cr=db.cursor()

class Employee:
	def __init__(self,eid=0,ename=0,esalary=0,des=0,mob=0,gender=0):
		self.eid=eid
		self.ename=ename
		self.esalary=esalary
		self.des=des
		self.mob=mob
		self.gender=gender

	def Display(self):
		print("\t\t\t\t DETAILS OF THE EMPLOYEE  \t\t\t\t\n\n")
		print("\t\t Emplyoee id: ",self.eid,"\t\t Employee name: ",self.ename)
		print("\t\t Emplyoee salary: ",self.esalary,"\t\t Employee Designation: ",self.des)
		print("\t\t Emplyoee Mobile: ",self.mob,"\t\t Employee Gender: ",self.gender)
		print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n\n")

	def Insert(self):
		try:
			n=int(input("Enter no. of the data you want to insert: "))
			for i in range(n):
				self.ename=input("Enter employee name: ")
				for i in range(3):
					try:
						self.esalary=int(input("Enter your salary: "))
						flag=0
						break
					except ValueError:
						if i==2:
							print("Time out")
							flag=1

						else:
							print("salary should be in numbers")
							continue
				if flag==1:
					break
				
				self.des=input("Enter the designation: ")
				for i in range(3):
					try:
						self.mob=int(input("Enter mobile number: "))
						flag1=0
						break
					except:
						if i==2:
							print("Time out:")
							flag1=1
						else:
							print("mobile no. should be integer")
							continue
				if flag1==1:
					break
				self.gender=input("Enter the gender: ")
				cr.execute('insert into emp2(empname,empsalary,designation,mobileno,gender) values("{}",{},"{}",{},"{}")'.format(self.ename,self.esalary,self.des,self.mob,self.gender))
				db.commit()
				print("Data inserted succesfully")
		except:
				print("INPUT SHOULD BE INTEGER:")

	def Fetch(self):
		cr.execute('select* from emp2')
		data=cr.fetchall()
		return data



	def MaxNo(self):
		cr.execute('select max(empsalary) from emp2 where empsalary != (select max(empsalary) from emp2)')
		data2=cr.fetchall()
		return data2


	def MinNo(self):
		cr.execute('select min(empsalary) from emp2 where empsalary != (select min(empsalary) from emp2)')
		data3=cr.fetchall()
		return data3


	def Char(self):
		cr.execute("select* from emp2 where empname like 'a%'")
		d1=cr.fetchall()
		return d1
	def Char1(self):
		cr.execute("select* from emp2 where empname like '%h_'")
		d2=cr.fetchall()
		return d2
	def Char2(self):
		cr.execute("select* from emp2 where empname like '%u%'")
		d3=cr.fetchall()
		return d3


		