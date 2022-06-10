import sys
from math import sqrt
def overlap(x1=0,y1=0,r1=1,x2=0,y2=0,r2=1):
		dis=sqrt((x2-x1)**2+(y2-y1)**2)
		if dis<(r1+r2):
			return True
		return False


if __name__ == "__main__":
	main()