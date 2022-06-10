def overlap(x1=0,y1=0,r1=1,x2=0,y2=0,r2=1):
   r = r1 + r2
   x = ((x2 - x1) ** 2)
   y = ((y2 - y1) ** 2)
   l = ((x + y) ** 1/2)
   return(l < r)
   
