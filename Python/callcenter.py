import datetime
import itertools


class call(object):
	idnum = itertools.count(1)
	def __init__ (self,name,number,reason):
		self.idnum = next(self.idnum)
		self.name = name
		self.number = number
		self.time = datetime.datetime.now()
		self.reason = reason
	def display(self):
		return self.idnum, self.name, self.number, self.time, self.reason

call1 = call("Dionne",5555555,"lost car keys").display()
# print call1

call2 = call("Alex",4444444,"just to say hi").display()
# print call2

call3 = call("Jonah",123456789,"needs help picking out clothes").display()
# print call3

class callcenter(call):
	def __init__ (self):
		self.allcalls = []
		self.nextcalls = []
	def add(self,*x):
		self.allcalls.append(x)
		return self.allcalls
	def remove(self,x):
		self.nextcalls.__delitem__(x[0][0])


round1 = callcenter().add(call1,call2,call3)
print len(round1[0])

print callcenter().remove(round1)





