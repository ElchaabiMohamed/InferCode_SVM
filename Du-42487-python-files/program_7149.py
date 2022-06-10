import sys

def overlap(x1=0,y1=0,r1=0,x2=0,y2=0,r2=0):
	distance = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)
	radius = r1 + r2
	return radius < distance

if __name__ == '__main__':
	main()