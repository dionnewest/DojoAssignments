#find and replace
words = "It's thanksgiving day. It's my birthday, too!"
words2 = "day"

print words.find(words2)
print words[18]+words[19]+words[20]
print words.replace(words2, "month")

#min and max
x = [2,54,-2,7,12,98]
min = x[0]
max = x[0]
i = 1
for i in x:
	if i < min:
		min = i
	if i > max:
		max = i
print min, max

#first and last
x = ["hello",2,54,-2,7,12,98,"world"]
x = [x[0],x[len(x)-1]]
print x

#new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
y = []
z = []
x.sort()
print x
i = 0
while i < len(x)/2:
	y.append(x[i])
	i += 1
z.append(y)
while i< len(x):
	z.append(x[i])
	i +=1
print z



		

