#!/usr/bin/env python3

import sys
from math import sqrt

def distance(x1,y1,x2,y2):
	return sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
	#distance formula

def overlap(x1=0 , y1=0, r1=1, x2=0, y2=0, r2=1):
	dist = distance(x1,y1,x2,y2)
	return dist < r1 + r2

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
