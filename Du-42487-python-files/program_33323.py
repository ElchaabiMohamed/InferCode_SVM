import sys

def overlap(x1 = 0, y1=0, r1=1, x2=0, y2=0, r2=1):
    distance = ((x2 - x1)**2) + ((y2-y1)**2)
    summ = r1 + r2
    if summ**2 > distance:
        return True
    else:
        return False



if __name__ == '__main__':
    main()
