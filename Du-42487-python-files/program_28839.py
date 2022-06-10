#!/usr/bin/env python3

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def overlap(x1=0, y1=0, r1=1, x2=0, y=0, r2=1):
    return distance(x1, y1, x2, y2) < r1 + r2
