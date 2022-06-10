def overlap(x1 = 0, y1 = 0, r1 = 1, x2 = 0, y2 = 0, r2 = 1):
    x = x2 - x1
    y = y2 - y1
    r = r1 + r2
    hypotenuse = (x ** 2 + y ** 2) ** 0.5
    return(r > hypotenuse)
    

def main():
    print((overlap()))
    print((overlap(10)))
    print((overlap(10,10)))
    print((overlap(10,10,10)))
    print((overlap(10,0,10)))
    print((overlap(10,0,1,8,0,1)))
    print((overlap(10,0,1,8,0,2)))

if __name__ == '__main__':
    main()

