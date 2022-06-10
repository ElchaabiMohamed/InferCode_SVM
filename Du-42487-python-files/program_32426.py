def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
	x = (x2-x1)**2
	y =(y2-y1)**2
	distance = (x + y) // 2	
	print(distance)
	print((r1+r2))
	print((r1-r2))
	if r1 + r2 == distance:
		return True
	elif r1 - r2 == distance:
		return True
	else:
		return False
