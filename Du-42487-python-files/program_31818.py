def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    dis = (((x1 - x2)**2) + ((y1 - y2)**2))**0.5
    if (r1 + r2) >= dis and dis != 0:
        return True
    elif dis == 0 and r1 == r2:
        return True 
    else:
        return False