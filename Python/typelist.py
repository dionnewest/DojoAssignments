l = ["magical",10,10,10,"unicorns love you"]
y = []
i = 0
for i in l:
	y.append(type(i))

i = 0
for i in y:
	if i == y[0] and i == int:
		message = "The list you entered is of integer type."
	elif i == y[0] and i == str:
		message = "The list you entered is of string type."
	elif i == y[0] and i == float:
		message = "The list you entered is of float type."
	elif i != y[0]:
		message = "The list you entered is of mixed type."
		break
print message

i = 0
z = ["String:"]
for i in l:
	if type(i) == str:
		z.append(" "+i)

sentence = ""
if len(z) > 1:
	for i in z:
		sentence += i
	print sentence

i = 0
total = 0
x = ["Sum:"]

while i < len(l):
	if type(l[i]) == int or type(l[i]) == float:
		for i in l:
			total += i
		total=str(total)
		x.append(" "+total)
	else:
		x = ["Sum:"]
	i += 1

sentence = ""

if len(x) > 1:
	for i in x:
		sentence += i
	print sentence









