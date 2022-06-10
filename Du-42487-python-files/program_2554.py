import sys
from math import sqrt

def overlap(x1 = 0, y1 = 0, r1 = 1, x2 = 0, y2 = 0, r2 = 1):
	lenradii = r1 + r2
	distbtwnpoints = sqrt((x1 - x2)**2 + (y2 - y1)**2)
	return lenradii > distbtwnpoints

# print(overlap())
# print(overlap(10))
# print(overlap(10,10))
# print(overlap(10,10,10))
# print(overlap(10,0,10))
# print(overlap(10,0,1,8,0,1))
# print(overlap(10,0,1,8,0,2))