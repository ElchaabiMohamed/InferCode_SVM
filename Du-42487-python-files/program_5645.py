import sys

def overlap(x1,y1,r1,x2,y2,r2):
	d = ((x2-x1) ** 2 + (y2 - y1) ** 2) ** .5
	r = r1 + r2
	return r == d

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
