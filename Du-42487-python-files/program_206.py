def overlap(x1, y1, r1, x2, y2, r2):
	distance = ((((x2-x1)**2) + ((y2-y1)**2))//2)	
	if r1 + r2 == distance:
		return True
	elif r1 - r2 == distance:
		return True
	else:
		return False
