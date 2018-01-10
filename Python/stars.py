#Part I
def draw_stars(x):
	for i in range (0,len(x)):
		string = ""
		for a in range (0, x[i]):
			string += "*"
		print string

x = draw_stars([4, 6, 1, 3, 5, 7, 25])

#Part II
def draw_stars(x):
	for i in range (0,len(x)):
		string = ""
		if type(x[i]) == str:
			for a in range (0,len(x[i])):
				string += x[i][0]
			print string.lower()
		if type(x[i]) == int:
			for a in range (0,x[i]):
				string += "*"
			print string

x = draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])


