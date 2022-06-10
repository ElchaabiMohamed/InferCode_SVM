import math
def overlap(x1 = 0, y1 = 0, r1 = 1, x2 = 0, y2 = 0, r2 = 1):
	boolean_intersects = math.hypot(x2 - x1, y2 - y1) < (r1 + r2)
	return boolean_intersects
