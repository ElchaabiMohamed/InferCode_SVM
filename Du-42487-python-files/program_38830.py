

def overlap(x1=0,y1=0,r1=1,x2=0,y2=0,r2=1):
	a = (x2-x1)**2
	b = (y2-y1)**2
	dist = (a + b)**(1/2)
	radius_total = r1 + r2
	return dist < radius_total
