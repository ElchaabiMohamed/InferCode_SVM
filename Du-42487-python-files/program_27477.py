from math import sqrt
from collections import namedtuple
def distance(x1, y1, x2, y2):
	return sqrt((x2 - x1)**2 + (y2 - y1)**2)
def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
	return distance(x1, y1, x2, y2) < (r1 + r2)