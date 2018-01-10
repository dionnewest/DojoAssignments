import random
heads = 0
tails = 0
for i in range (1,11):
	toss = random.randint(1,2)
	if toss == 1:
		heads += 1
		print "Attempt #"+str(i)+": Throwing a coin... it's a head!... Got "+str(heads)+" heads(s) so far and "+str(tails)+" tail(s) so far"
	elif toss == 2:
		tails += 1
		print "Attempt #"+str(i)+": Throwing a coin... it's a head!... Got "+str(heads)+" heads(s) so far and "+str(tails)+" tail(s) so far"
