def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    import math
    d=math.sqrt((x2 - x1) ** 2 + (y2 - x1) ** 2)
    if (r1+ r2) >= d:
        return True
    else:
        return False

