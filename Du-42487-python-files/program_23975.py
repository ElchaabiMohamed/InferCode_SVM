import sys

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
   return float(((x2 - x1) + (y2 - y1)) ** 0.5) < float(r1 + r2)
   #return x1,y1,r1,x2,y2,r2

