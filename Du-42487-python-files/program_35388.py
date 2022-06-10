import sys

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
   distance = ((x2 - x1) + (y2 - y1)) ** .5 / 2
   radii = r1 + r2
   print((distance, radii))

