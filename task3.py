import mysql.connector as ms

db=ms.connect(host="localhost", user="root", password="root", database="emp")
cr=db.cursor()
while True:
	print("""
press 1 for insert data:
press 2 for print all data:
press 3 for search the data by employee id:
press 0 for exit:

#fetch detail by emp detail
#fetch all detail
	""")
	n=input("Enter the option:")
	if n=='1':
		cr.execute('select empid from emp1')
		data=cr.fetchall()
		ls=[]
		for i in data:
			ls.append(i[0])
		name=input("Enter name:")
		for i in range(3):
			empi=input("Enter employee id:")
			if empi in ls:
				if i==2:
					print("duplicate employee id is not supported")
					print("Time out")
				elif empi in ls:
					print("duplicate employee id is not supported")
					continue
				
				else:
					break
					
			else:
				break
		if empi in ls:
			continue
				
		dep=input("Enter the department:")
		profile=input("Enter profile:")
		dob=input("Enter Date of birth:")
		sal=int(input("Enter the salary:"))
		city=input("Enter the city:")
		cr.execute('insert into emp1(name,empid,department,profile,dob,salary,city) values("{}","{}","{}","{}","{}",{},"{}")'.format(name,empi,dep,profile,dob,sal,city))
		db.commit()
		print("Data insert succesfull")
	elif n=='2':
		cr.execute('select* from emp1')
		data=cr.fetchall()
		for i in data:
			print("\n\n------------------------------------------------------------------------------------------")
			print("s-no:",i[0],"\t\t Name=",i[1])
			print("e-id:",i[2],"\t\t Department=",i[3])
			print("Profile:",i[4],"\t\t D-O-B=",i[5])
			print("Salary:",i[6],"\t\t city=",i[7])
			print("\n\n------------------------------------------------------------------------------------------")
	elif n=='3':
		n=input("Enter employee id:")
		cr.execute('select* from emp1')
		data=cr.fetchall()
		list=[]
		for x in data:
			list.append(x[2])
		for i in data:
			if n==i[2]:
				print("\n\n------------------------------------------------------------------------------------")
				print("s-no:",i[0],"\t\t Name=",i[1])
				print("e-id:",i[2],"\t\t Department=",i[3])
				print("Profile:",i[4],"\t\t D-O-B=",i[5])
				print("Salary:",i[6],"\t\t city=",i[7])
				print("\n\n------------------------------------------------------------------------------------")
				
		if n not in list:
				print("This employee id is not in the data")	
	elif n=='0':
		break

	else:
		print("wrong option")