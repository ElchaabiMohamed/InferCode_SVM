import sys
from math import hypot

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    distance = hypot(x2 - x1, y2 - y1)
    return distance < r1 + r2