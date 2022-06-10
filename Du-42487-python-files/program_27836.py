import math

def overlap(x1=0,y1=0,r1=1,x2=0,y2=0,r2=1):
    d = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    if d <= r1+r2:
        return True
    # return d

def main():
    print((overlap(10,0,1,8,0,2)))


if __name__ == '__main__':
    main()
