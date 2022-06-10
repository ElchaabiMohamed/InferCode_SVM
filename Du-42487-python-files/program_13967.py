import sys

def overlap(x1, y1, r1, x2, y2, r2):
	if r1+r2 >= (((x2 -x1)**2) +((y2 - y1)**2))**0.5:
		return True
	else :
		return False







x1 = 0
y1 = 0
r1 = 1
x2 = 0
y2 = 0
r2 = 1