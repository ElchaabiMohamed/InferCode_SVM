import sys
import math
def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
	
	sumrad = r1 + r2
	xs = (x2 - x1)**2
	ys = (y2 - y1)**2
	inside = xs + ys
	dis = math.sqrt(inside)
	if dis < sumrad:
		return(True)
	elif sumrad < dis:
		return(False)
	elif sumrad == dis:
		return(False)



