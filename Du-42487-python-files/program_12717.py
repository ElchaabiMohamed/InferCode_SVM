import sys

def overlap(x1, y1, r1,x2,y2,r2):
	distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2))
	radius = r1 + r2
	return radius < distance

if __name__ == '__main__':
	main()