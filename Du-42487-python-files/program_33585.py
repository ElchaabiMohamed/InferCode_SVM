import sys
import math
def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
	try:
		overlap=False
		if math.sqrt((x1-x0)**2+(y1-y0)**2) < (R0+R1):
			overlap=True
		return(overlap)
	except TypeError:
		pass
	
def main():
    print((overlap()))
    print((overlap(10)))
    print((overlap(10,10)))
    print((overlap(10,10,10)))
    print((overlap(10,0,10)))
    print((overlap(10,0,1,8,0,1)))
    print((overlap(10,0,1,8,0,2)))
    print((overlap(10.0,0.0,1.0,8.1,0.1,2.2)))


if __name__ == '__main__':
    main()


