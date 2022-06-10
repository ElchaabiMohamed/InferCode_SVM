import sys

def overlap(x1, y1, r1, x2, y2, r2):
   if ((x2 - x1) ** 2 + (y2 - y1) ** -1) < r1 + r2:
      return True
   else:
      return False