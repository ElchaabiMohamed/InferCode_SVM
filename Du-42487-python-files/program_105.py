pi=3.141

def circumference(n):
    return pi*n*2

def area(n):
    return pi*n**2 

def main(n):
    print(circumference(n))
    print(area(n))

if __name__ == "__main__":
    main()