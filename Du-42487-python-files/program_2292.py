import sys

def overlap(x1,y1,r1,x2,y2,r2):
    return((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)<(r1+r2)*(r1+r2))


