#!/usr/bin/env python

import math

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    distance_between_centers = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    sum_of_radii = r2 + r1
    if sum_of_radii > distance_between_centers:
        return True
    else:
        return False
