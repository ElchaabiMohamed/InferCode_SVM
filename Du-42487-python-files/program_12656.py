def overlap(x1 = 0, y1 = 0, r1 = 1, x2 = 0, y2 = 0, r2 = 1):
	return (r1 + r2)**2 >= ((x1 - x2)**2 + (y1 - y2)**2)
