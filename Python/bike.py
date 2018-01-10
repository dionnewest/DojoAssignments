class bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print self.price
		print self.max_speed
		print self.miles
		return self
	def ride(self):
		self.miles += 10
		print "Riding " + str(self.miles)
		return self
	def reverse(self):
		if self.miles >= 5:
			self.miles -= 5
		print "Reversing " + str(self.miles)
		return self

bike1 = bike(200,"25mph").ride().ride().ride().reverse().displayInfo()
bike2 = bike(250,"30mph").ride().ride().reverse().reverse().displayInfo()
bike3 = bike(199,"26mph").reverse().reverse().reverse().displayInfo()



