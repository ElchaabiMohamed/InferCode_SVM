import sys

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
	a = abs(x2 - x1)
	o = abs(y2 - y1)
	h2 = a**2 + o**2
	h = h2**0.5
	return h < r1 + r2