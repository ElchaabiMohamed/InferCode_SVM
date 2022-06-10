def maximum(l):
	highest = "null"
	for c in l:
		if highest == "null":
			highest = c
		elif c > highest:
			highest = c
	return highest		
