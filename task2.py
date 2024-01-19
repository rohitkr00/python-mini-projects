import mysql.connector as ms

db=ms.connect(host="localhost", user="root", password="root", database="login")
cr=db.cursor()
while True:
	print("""
press 1 for sign up:
press 2 for sign in:
press 0 for exit:
	""")
	n=input("Enter the option:")
	if n=='1':
		user=input("Enter user name:")
		pas=input("Enter password:")
		cr.execute('select* from login')
		data=cr.fetchall()
		try:
			cr.execute('insert into login values("{}","{}")'.format(user,pas))
			db.commit()
			print("Sign up is succesfull")
		except:
			print("user name is already registerd")

	elif n=='2':
		user=input("Enter user name:")
		cr.execute('select * from login')
		data=cr.fetchall()
		ls=[]
		for i in data:
			ls.append(i[0])
		if user not in ls:
			print("Wrong user name")
			break
		for i in range(4):
			if i==0 or i==1 or i==2:
				pas=input("Enter password:")
				cr.execute('select * from login')
				data=cr.fetchall()
				if (user,pas) in data:
					print("sign in sucessful")
					break
				else:
					print("wrong password rennter password")
					continue
			else:
				print("Time out")
				break
			
			
				
				
			
	elif n=='0':
		break
	else:
		print("choose correct option")