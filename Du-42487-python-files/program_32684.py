import sys
import math
def overlap(x0=0, y0=0, R0=1, x1=0, y1=0, R1=1):
	try:
		overlap=True
		if math.sqrt((int(x0)-int(x1))**2+(int(y0)-int(y1))**2) < (int(R0)+int(R1)):
			overlap=False
		return(overlap)
	except TypeError:
		print(False)
	
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


