#!usr/bin/env python3


def point_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    return point_distance(x1, y1, x2, y2) < (r1 + r2)
