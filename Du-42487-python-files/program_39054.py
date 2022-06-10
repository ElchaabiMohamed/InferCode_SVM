#!/usr/bin/env python3

# specifies six parameters in the following order: 
# x1, y1, r1, x2, y2, r2

# default radius = 1
# default x & y = 0
def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    distance = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
    radius = r1 + r2
    return distance < radius