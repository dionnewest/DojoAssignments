class animal(object):
	def __init__ (self,name,health):
		self.name = name
		self.health = health
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def display_health(self):
		print self.health

animal1 = animal('cat', 100).walk().walk().run().run().display_health()

class dog(animal):
	def __init__ (self,name):
		super(dog, self).__init__ (name, 150)
	
	def pet(self):
		self.health += 5
		return self

animal2 = dog('dog').walk().walk().walk().run().run().pet().display_health()

class dragon(animal):
	def __init__ (self,name):
		super(dragon, self).__init__ (name, 170)
	def fly(self):
		self.health -= 10
		return self
	def display_health(self):
		print "I am a Dragon " + str(self.health)

animal3 = dragon('sparky').fly().fly().fly().display_health()

animal4= animal('kitten',100).walk().run().display_health()

animal5= dog('O').pet().display_health()
