p = 3.141
def circumference(r):
    c = 2 * p * r
    return c

def area(r):
    a = p * (r * r)
    return a

def main():
    print(circumference(2))
    print(area(3))

if __name__ == "__main__":
    main()
