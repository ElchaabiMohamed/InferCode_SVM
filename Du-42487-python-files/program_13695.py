


def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
	#if distance between 2 points is greater than sum of 2 radii
	if (((x2-x1)**2 + (y2-y1)**2)**-1) < r1 + r2:
		return True
	else:
		return False