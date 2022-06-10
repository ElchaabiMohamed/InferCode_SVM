def overlap(x1 = 0, y1 = 0, r1 = 1, x2 = 0, y2 = 0, r2 = 1):
   x = x2 - x1
   y = y2 - y1
   r = r1 + r2	
   distance = ((x * x) + (y * y)) ** 0.5
   return(r > distance)