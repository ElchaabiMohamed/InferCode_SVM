import sys
import math

def overlap(x1=0,y1=0,r1=1,x2=0,y2=0,r2=1):
   dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
   radsum = (r1 + r2)**2
   raddif = (r1 - r2)**2
   if dist < radsum and dist > raddif:
      return True
   return False