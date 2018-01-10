# ODD/EVEN
for i in range (1,201):
	if i % 2 == 0:
		print "Number is "+str(i)+". This is an even number."
	if i % 2 == 1:
		print "Number is "+str(i)+". This is an odd number."

# MULTIPLY
def multiplied(a,c):
	for i in range (0,len(a)):
		a[i] = a[i]*c
	return a
a = [2,4,10,16]
c = 5
b = multiplied(a,c)
print b

# HACKER CHALLENGE
def layered_multiples(arr):
  	new_array=[]
  	for i in range (0,len(arr)):
  		new_array.append([])
  		for x in range (0,arr[i]):
  			new_array[i].append(1)
  	return new_array
arr = [2,4,5]
c = 3
x = layered_multiples(multiplied(arr,c))
print x
