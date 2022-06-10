from math import sqrt

def overlap(x1, y1, r1, x2, y2, r2):
	return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) < r1 + r2