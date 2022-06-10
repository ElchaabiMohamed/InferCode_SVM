import sys
import math

def overlap(x1 = 0, y1=0, r1=1, x2=0, y2=0, r2=1):
    distance = sqrt((x2 - x1)**2 + (y2-y1)**2)
    dif = r1 -r2
    summ = r1 + r2
    if dif <= distance and summ >= distance:
        return True
    else:
        return False




if __name__ == '__main__':
    main()
