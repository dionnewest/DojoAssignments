list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','milk']
matches = 0
i = 0
if len(list_one) == len(list_two):
	while i < len(list_one):
		if list_one[i] == list_two[i]:
			matches += 1
		else:
			break
		i = i + 1

if matches == len(list_one):
	print "The lists are the same"
else:
	print "The lists are not the same"