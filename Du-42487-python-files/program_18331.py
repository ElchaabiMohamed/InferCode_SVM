def overlap(x1 = 0, y1 = 0, r1 = 1, x2 = 0, y2 = 0, r2 = 1):
	r = x2 - x1
	
	f = y2 - y1
	
	rf = (r**2 + f**2)**0.5
	
	if r == 0 and f == 0:
		return "True"
	elif r1 + r2 >  rf:
		return "True"
	else:
		return "False"