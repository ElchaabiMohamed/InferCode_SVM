#!/usr/bin/env python3

import sys

def overlap(x1=0, y1=0, r1=0, x2=0, y2=0, r2=0):
	dist = ( (x2 - x1)**2 + (y2 - y1)**2) **1/2
	return dist <= (r1 + r2)

def main():

    print((overlap()))
    print((overlap(10)))
    print((overlap(10,10)))
    print((overlap(10,10,10)))
    print((overlap(10,0,10)))
    print((overlap(10,0,1,8,0,1)))
    print((overlap(10,0,1,8,0,2)))

if __name__ == "__main__":
   main()