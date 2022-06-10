def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    import math
    r= r1 + r2
    d=math.sqrt((x2 - x1) ** 2 + (y2 - x1) ** 2)
    print((r, d))
    if r > d:
        return True
    else:
        return False

