pi = 3.141

def circumference(r):
    circ = 2 * pi * r
    return circ
    
def area(r):
    ar = (r ** 2) * pi
    return ar
    
def main():
    print(circumference(3))
    print(area(4))
    
if __name__ == "__main__":
    main()