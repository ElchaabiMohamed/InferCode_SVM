def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    if x1 + y1 + x2 + y2 + r1 + r2 == 0:
       return True
    else:
       return ((x2 - x1)**2 + (y2 - y1)**2) < (r1+r2)**2