message = " "
for i in range (1,13):
	i = str(i)
	message += " "+i
	i = int(i)
print "x" + message

for x in range (1,13):
	x = str(x)
	message = x
	x = int(x)
	for i in range (1,13):
		i = i*x
		i = str(i)
		message += " "+i
		i = int(i)
	print message


	

