import math

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
	if distance(x1, y1, x2, y2) < r1 + r2:
		return  True
	else:
		return  False

def distance(x1, y1, x2, y2):
	disx = (x2 -x1)**2
	disy = (y2 -y1)**2
	dist = disx + disy
	return math.sqrt(dist)

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