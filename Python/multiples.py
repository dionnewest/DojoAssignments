i = 1
while i < 1000:
	if i%2 == 1:
		print i
	i += 1

for i in range(1,1000):
	if i%2 == 1:
		print i


i = 5
while i <= 1000000:
	if i%5 == 0:
		print i
	i += 1

for i in range (5,1000001):
	if i%5 == 0:
		print i

a = [1,2,5,10,255,3]
i = 1
sum = a[0]
for i in a:
	sum = sum + i
print sum

a = [1,2,5,10,255,3]
i = 1
sum = a[0]
for i in a:
	sum = sum + i
avg = sum/len(a)
print avg