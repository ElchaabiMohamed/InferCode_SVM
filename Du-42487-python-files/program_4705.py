import sys
from math import sqrt


def overlap(x1=0,y1=0,r1=0,x2=0,y2=0,r2=0):
    distance = sqrt(((x2-x1)**2) + ((y2 - y1)**2))
    radii = (r1 + r2)
    return distance >= radii
    