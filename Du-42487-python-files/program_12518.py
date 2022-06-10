import sys

def overlap(x1=None,y1=None,r1=None,x2=None,y2=None,r2=None):
	if x1 is None:
		x1 = 0
	if y1 is None:
		y1 = 0
	if r1 is None:
		r1 = 1
	if x2 is None:
		x2 = 0
	if y2 is None:
		y2 = 0
	if r2 is None:
		r2 = 1
	
	c = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
	if c > r1 or c > r2:
		return False
	else:
		return True