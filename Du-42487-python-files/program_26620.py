pi = 3.141

def circumference(r):
    return float(2 * pi * r)

def area(r):
    return float(pi * (r ** 2))

def main(r):
    print(circumference(5))


if __name__ == "__main__":
    main()
