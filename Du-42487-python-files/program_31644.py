import sys

def dist(x1,y1,x2,y2):
	return (((x2-x1)**2) + ((y2-y1)**2))**0.5

def overlap(x1,y1,r1,x2,y2,r2):
	return dist(x1,y1,x2,y2) < r1 + r2

if __name__ == "__main__":
   main()