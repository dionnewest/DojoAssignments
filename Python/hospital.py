import itertools

class patient(object):
	idnum = itertools.count(1)
	bed_number = itertools.count(101)
	def __init__ (self):
		self.name = name
		self.idnum = next(self.idnum)
		self.allergies = allergies
		self.bed_number = next(self.bed_number)
	def admit (self,name,allergies):
		return self.bed_number


class hospital(patient):
	def __init__ (self):
		super(patient, self).__init__ ():
		self.hospital_name = "General Hospital"
		self.patients = []
		self.capacity = 100
