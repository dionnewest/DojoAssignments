class Building(object):
	def __init__(self, height, width, address, color, roof, occupancy, age, door):
		self.height = height
		self.width = width
		self.address = address
		self.color = color
		self.roof = roof
		self.occupancy = occupancy
		self.age = age
		self.door = door

	def toggleDoor(self):
		self.door = not self.door
		return self

	def __repr__(self):
		return "{} {} {} {} {} {} {} {}".format(self.height, self.width, self.address, self.color, self.room, self.occpancy)

		