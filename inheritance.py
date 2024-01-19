class Media:
	def __init__(self,title=0,size=0,price=0):
		self.title=title
		self.size=size
		self.price=price


	def Display(self):
		print("Title=",self.title)
		print("Size=",self.size)
		print("Price=",self.price)

class Dvd(Media):
	def __init__(self,title=0,size=0,price=0):
	 Media.__init__(self,title,size,price)

	def Display(self):
		Media.Display(self)

class eBook(Media):
	def __init__(self,title=0,size=0,price=0,pub=0,auth=0):
		Media.__init__(self,title,size,price,pub,auth)
		self.pub=pub
		self.auth=auth

	def Display(self):
		Media.Display(self)
		print("Author=",self.auth)
		print("pub=",self.pub)


ob=Dvd("english","3gb",150)
ob.Display()





