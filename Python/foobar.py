for i in range (1, 11):
	if i > 1:
		for x in range (2,i):
			if(i % x == 0 and i == x):
				print "Bar"
				break
			if(i % x == 0):
				print "FooBar"
				break
			else:
				print "Foo"
	else:
		print "Foo"



