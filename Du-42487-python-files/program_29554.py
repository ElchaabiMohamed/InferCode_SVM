
import math

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
	r = r1 + r2
	centre = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
	return centre >= r

