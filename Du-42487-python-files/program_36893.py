import math as maths

def overlap(x1=0, y1=1, r1=0, x2=0, y2=0, r2=0):
    distance = maths.sqrt((x2-x1)^2 + (y2-y1)^2)
    return distance < (r1 + r2)
