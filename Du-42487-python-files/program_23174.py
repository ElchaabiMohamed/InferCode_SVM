import sys
import math
def overlap(x0=0, y0=0, R0=1, x1=0, y1=0, R1=1):
	overlap=False
	if sqrt((x0-x1)**2+(y0-y1)**2) < (R0+R1):
		overlap=True
	return(overlap)
		
def main():
    print((overlap()))
    print((overlap(10)))
    print((overlap(10,10)))
    print((overlap(10,10,10)))
    print((overlap(10,0,10)))
    print((overlap(10,0,1,8,0,1)))
    print((overlap(10,0,1,8,0,2)))


if __name__ == '__main__':
    main()


