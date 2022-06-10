def overlap(x1=None,y1=None,r1=None,x2=None,y2=None,r2=None):
    if x1 is None:
        x1 = 0
    if y1 is None:
        y1 = 0
    if r1 is None:
        r1 = 1
    if x2 is None:
        x2 = 0
    if y2 is None:
        y2 = 0
    if r2 is None:
        r2 =1

    return (x1 - x2) ** 2 + (y1 - y2) ** 2 < (r1 + r2) ** 2


def main():
    print((overlap()))
    print((overlap(10)))
    print((overlap(10, 10)))
    print((overlap(10, 10, 10)))
    print((overlap(10, 0, 10)))
    print((overlap(10, 0, 1, 8, 0, 1)))
    print((overlap(10, 0, 1, 8, 0, 2)))


if __name__ == "__main__":
    main()