from emp import Employee
'''
import mysql.connector as ms
db=ms.connect(host="localhost", user="root", password="root", database="emp")
cr=db.cursor()
'''

def Program():
	while True:
		print("""
press 1 for insert data:
press 2 for show all data:
press 3 for whoose salary is gretar than 15000:
press 4 for whoose salary is less than 7000:
press 5 for whoose salary is gretar than 12000:
press 6 for whoose designation is manager:
press 7 for total salary of clerk
press 8 for second highest salary
press 9 for second min salary
press 10 for name start with 'A'
press 11 for the second last charcter should be 'h'
press 12 for the 'u' in charcter
press 0 for exit:

		""")

		n=input("Enter the choice: ")
		if n=="1":
			ob=Employee()
			ob.Insert()
			
	

		elif n=="2":
			ob=Employee()
			d=ob.Fetch()
			for i in d:
				ob2=Employee(i[0],i[1],i[2],i[3],i[4],i[5])
				ob2.Display()


		elif n=="3":
			ob=Employee()
			d=ob.Fetch()
			for i in d:
				if i[2]>15000:
					ob2=Employee(i[0],i[1],i[2],i[3],i[4],i[5])
					ob2.Display()



		elif n=="4":
			ob=Employee()
			d=ob.Fetch()
			for i in d:
				if i[2]<7000:
					ob2=Employee(i[0],i[1],i[2],i[3],i[4],i[5])
					ob2.Display()
	
		elif n=="5":
			ob=Employee()
			d=ob.Fetch()
			for i in d:
				if i[2]>12000:
					ob2=Employee(i[0],i[1],i[2],i[3],i[4],i[5])
					ob2.Display()


		elif n=="6":
			ob=Employee()
			d=ob.Fetch()
			for i in d:
				if i[3]=="Manager":
					ob2=Employee(i[0],i[1],i[2],i[3],i[4],i[5])
					ob2.Display()


		elif n=="7":
			ob=Employee()
			d=ob.Fetch()
			sum=0
			for i in d:
				if i[3]=="Clerk":
					sum=sum+i[2]
			print("Total salary of clerk is: ",sum)

		elif n=="8":
			ob=Employee()
			d=ob.Fetch()
			d2=ob.MaxNo()
			for i in d:
				if i[2]==d2[0][0]:
					ob2=Employee(i[0],i[1],i[2],i[3],i[4],i[5])
					ob2.Display()

		elif n=="9":
			ob=Employee()
			d=ob.Fetch()
			d2=ob.MinNo()
			for i in d:
				if i[2]==d2[0][0]:
					ob2=Employee(i[0],i[1],i[2],i[3],i[4],i[5])
					ob2.Display()

		elif n=="10":
			ob=Employee()
			d=ob.Char()
			for i in d:
				ob2=Employee(i[0],i[1],i[2],i[3],i[4],i[5])
				ob2.Display()

		elif n=="11":
			ob=Employee()
			d=ob.Char1()
			for i in d:
				ob2=Employee(i[0],i[1],i[2],i[3],i[4],i[5])
				ob2.Display()

		elif n=="12":
			ob=Employee()
			d=ob.Char2()
			for i in d:
				ob2=Employee(i[0],i[1],i[2],i[3],i[4],i[5])
				ob2.Display()

		elif n=="0":
			break
	
		else:
			print("Chose correct option")


Program()






		

		