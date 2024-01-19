class vehicle:
	def __init__(self,color,size,capacity):
		color=input("Enter color: ")
		size=input("Enter size: ")
		capacity=input("Enter capacity: ")
		self.color=color
		self.size=size
		self.capacity=capacity

	def Display(self):
		print("Color: ",self.color)
		print("Size: ",self.size)
		print("Capacity: ",self.capacity)

class TwoWheeler(vehicle):
	def __init__(self,color=0,size=0,capacity=0,company=0,milage=0):
		vehicle.__init__(self,color,size,capacity)
		milage=input("Enter milage: ")
		company=input("Enter company: ")
		self.company=company
		self.milage=milage

	def Diplay(self):
		vehicle.Display(self)
		print("Company: ",self.company)
		print("milage: ",self.milage)

class ThreeWheelar(vehicle):
	def __init__(self,color,size,capacity,company,milage=0):
		vehicle.__init__(self,color,size,capacity,company,milage)
		milage=input("Enter milage: ")
		company=input("Enter company: ")
		self.company=company
		self.milage=milage

	def Diplay(self):
		vehicle.Display(self)
		print("Company: ",self.company)
		print("milage: ",self.milage)


class Bike(TwoWheeler):
	def __init__(self,color=0,size=0,capacity=0,company=0,milage=0,type=0,engine=0,gear=0):
		TwoWheelar.__init__(self,color,size,capacity,company,milage)
		type=input("Enter type of Bike: ")
		engine=input("Enter Engine cc of bike: ")
		gear=input("Enter no. of gear: ")
		self.type=type
		self.engine=engine
		self.gear=gear

	def Display(self):
		TwoWheelar.Display(self)
		print("Type: ",self.type)
		print("Engine capacity: "self.capacity)
		print("No. of gear: "self.gear)

	
