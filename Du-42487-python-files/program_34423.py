import sys
import math

def overlap(x1=0 , y1=0 , r1=1 , x2=0 , y2=0 , r2=1):
	if math.sqrt((x2 + y2) + (x1 + y1)) < math.sqrt((r2 + r1)) < math.sqrt((x2 - y2) + (x1 - y1)):
		return True
	else:
		return False