
def overlap(x1, y1, r1, x2, y2, r2):
	d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
	r = r1 + r2
	return d >= r or d < r

