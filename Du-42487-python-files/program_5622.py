import sys
import math
def overlap(x1=0,y1=0,r1=1,x2=0,y2=0,r2=1):
	x=(x2-x1)*(x2-x1)
	y=(y2-y1)*(y2-y1)
	xy=x+y
	D=math.sqrt(xy)
	if D >= r1+r2:
		print(False)
	else:
		print(True)
