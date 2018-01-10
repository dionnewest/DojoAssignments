word_list = ['hello','world','my','name','is',"Thor"]
new_list = []
char = 'o'

for i in word_list:
	if char in i:
		new_list.append(i)
	else:
		continue

print new_list