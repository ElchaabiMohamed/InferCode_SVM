import sys
from math import sqrt

def overlap(x1 = 0, y1 = 0, r1 = 1, x2 = 0, y2 = 0, r2 = 1):
	lenradii = r1 + r2
	distancebtwnpoints = sqrt((x1 - x2)**2 + (y2 - y1)**2)
	return lenradii > distancebtwnpoints