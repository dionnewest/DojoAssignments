x = ["happy", 10, "unicorns", 10, "love", 10, "you"]
strings = 0
integers = 0
floats = 0
y = []
z = []
for i in x:
	if isinstance(i,str):
		y.append(i)
		strings += 1
	if isinstance(i,int):
		z.append(i)
		integers += 1
	if isinstance(i, float):
		z.append(i)
		floats += 1

if strings == len(x):
	message = "The list you entered is of string type."
elif integers == len(x):
	message = "The list you entered is of integer type."
elif floats == len(x):
	message = "The list you entered is of float type."
else:
	message = "The list you entered is of mixed type."
print message

i = 0
message1 = "String:"
message2 = "Sum:"
total = 0
for i in x:
	if type(i) == str:
		message1 += " " + i
	if type(i) == int or type(i) == float:
		total += i
if strings > 0:
	print message1
if integers > 0 or floats > 0:
	message2 += " " + str(total)
	print message2
