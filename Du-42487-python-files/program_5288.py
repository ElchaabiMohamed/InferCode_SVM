def overlap(x1=None, y1=None, r1=None, x2=None, y2=None, r2=None):
	if x1 == None:
		x1 = 0
	if y1 == None:
		y1 = 0
	if r1 == None:
		r1 = 1
	if x2 == None:
		x2 = 0
	if y2 == None:
		y2 = 0
	if r2 == None:
		r2 = 1
	distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
	return distance < r1 + r2