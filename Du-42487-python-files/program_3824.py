import math

def overlap(x1 = 0 , y1 = 0 , r1 = 1 , x2 = 0 , y2 = 0 , r2 = 1 ):
	#return square root of x's take y's doubled


	size = math.floor(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
	return size < r1 + r2 