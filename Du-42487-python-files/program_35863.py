from math import sqrt

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
	x = (x2-x1)**2
	y =(y2-y1)**2
	distance = sqrt(x + y)
	if (((r1 + r2) == distance or abs(r1 - r2) == distance) and (distance <= r1+r2-1)):
		return True
	else:
		return False
