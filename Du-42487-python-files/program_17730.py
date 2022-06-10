def overlap(x1=0, y1=0, r1=0, x2=0, y2=0, r2=0):
   dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
   return dist < (r1 + r2)
