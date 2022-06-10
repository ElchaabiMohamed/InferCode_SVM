def circumference(r):
    r = 2 * 3.141 * r
    return r
    
def area(r):
    r = r ** 2
    r = 3.141 * r 
    return r
    
    
def main():
    print(circumference(5))
    print(area(5))
    print(area(0.5))
    
if __name__ == "__main__":
    main()