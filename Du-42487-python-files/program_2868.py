#!/usr/bin/env pyhton3

import sys

def overlap(x1, y1 ,r1 ,x2 ,y2 ,r2):
	dist =  (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** .5
	if r1 + r2 >= dist:
		return False
	else:
		return True
