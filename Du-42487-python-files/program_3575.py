def circumference(r):
    circ = 2 * 3.141 * r
    return circ
    
def area(r):
    ar = (r ** 2) * 3.141
    return ar
    
def main():
    print(circumference(3))
    print(area(4))
    
if __name__ == "__main__":
    main()