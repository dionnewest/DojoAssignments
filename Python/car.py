class car(object):
	def __init__(self,price,speed,fuel,mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
	def display_all(self):
		print "CAR SUMMARY"
		print "Price: " + str(self.price)
		print "Speed: " + str(self.speed) +"mph"
		print "Fuel: " + self.fuel
		print "Mileage: " + str(self.mileage) +"mpg"
		print "Tax: " + str(self.tax)
		return self
car1 = car(2000,35,"Full",15).display_all()
car2 = car(2000,5,"Not Full",105).display_all()
car3 = car(2000,15,"Kind of Full",95).display_all()
car4 = car(2000,25,"Full",25).display_all()
car5 = car(2000,45,"Empty",25).display_all()
car6 = car(20000000,35,"Empty",15).display_all()
