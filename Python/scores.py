import random
print "Scores and Grades"
for n in range (0,10):
	random_num = random.randint(60,100)
	if random_num >= 90:
		print "Score: "+str(random_num)+"; Your grade is A"
	elif random_num >= 80 and random_num <90:
		print "Score: "+str(random_num)+"; Your grade is B"
	elif random_num >= 70 and random_num <80:
		print "Score: "+str(random_num)+"; Your grade is C"
	elif random_num >= 60 and random_num <70:
		print "Score: "+str(random_num)+"; Your grade is D"
	elif random_num >= 50 and random_num <60:
		print "Score: "+str(random_num)+"; Your grade is E"
	elif random_num < 50:
		print "Score: "+str(random_num)+": Your grade is F."
print "End of the program. Bye!"



