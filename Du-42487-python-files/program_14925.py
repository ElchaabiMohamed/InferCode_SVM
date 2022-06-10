import sys

def overlap(x1=0,y1=0,r1=1,x2=0,y2=0,r2=1):

	distance = (((x2-x1)**2) + ((y2-y1)**2))**0.5
	if float(r1) > distance-r2 and float(r2) > distance-r1:
		return(True)
	else:
		return(False)

