import sys
def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    from math import sqrt
    print((x1, y1, r1, x2, y2, r2))
    dist = sqrt((x2 -x1)**2 + (y2 -y1)**2)

def main():
    overlap()



if __name__ == '__main__':
    main()


