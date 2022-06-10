def overlap(x1 = 0 , y1 = 0, r1 = 1 , x2 = 0, y2 = 0 , r2 = 1 ): 
	dist = (((x2 - x1)**2) ** 0.5) + ((y2 - y1)**2)
	if dist < (r1 + r2):
	 	return True
	else:
	 	return False

