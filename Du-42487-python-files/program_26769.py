def minimum(l):
	lowest = "null"
	for c in l:
		if lowest == "null":
			lowest = c
		elif c < lowest:
			lowest = c
	return lowest		
