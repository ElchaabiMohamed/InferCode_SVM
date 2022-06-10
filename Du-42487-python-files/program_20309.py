#!/usr/bin/env python3
import sys
from math import sqrt

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
	c1c2 = sqrt((x1 - x2)**2 + (y1 - y2)**2)
	if c1c2 < r1 + r2:
		return True
	else:
		return False
