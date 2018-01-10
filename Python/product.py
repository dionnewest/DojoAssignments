class product(object):
	def __init__(self,price,item_name,weight,brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"
	def sell(self,tax):
		self.status = "sold"
		tax = 1 + tax
		self.price = self.price*tax
		return self
	def refund(self, reason, tax):
		tax = 1 + tax
		if reason == "defective":
			self.status = "defective"
			self.price = 0
		if reason == "unopenned":
			self.status = "for sale"
			self.price = self.price/tax
		if reason == "openned":
			self.status = "used"
			self.price = self.price/tax*.8
		return self
	def displayInfo(self):
		print self.price
		print self.item_name
		print self.weight
		print self.brand
		print self.status
		return self

# product1 = product(10,'Planner',.1,'Kate Spade').sell(.06).displayInfo()
product2 = product(100,'Textbook',1,'Scholastic').sell(.06).refund("openned",.06).displayInfo()
