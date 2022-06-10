import sys
def overlap(x1 = 0,y1 = 0,r1 = 1,x2 = 0,y2 = 0,r2= 1):
	a = ((x2 - x1) ** 2)
	b = ((y2 - y1) ** 2)
	c = ((a + b)** 0.5)
	total_r = (r1 + r2)

	if c < total_r:
		return True
	else:
		return False


