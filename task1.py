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
		pas=input("Enter password:")
		cr.execute('select* from login')
		data=cr.fetchall()
		if (user,pas) in data:
			print("sign in sucessful")
		else:
			print("wrong user name or password")
			
	elif n=='0':
		break
	else:
		print("choose correct option")