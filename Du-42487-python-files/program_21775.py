import math

def overlap(x1= 0, y1 = 0, r1 = 0, x2= 0, y2 = 0, r2 = 1):
	intersect = math.hypot(x1 - x2, y1 - y2) < (r1 + r2)
	return intersect