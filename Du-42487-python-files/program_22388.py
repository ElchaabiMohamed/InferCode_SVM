def circumference(r):
    a = 2 * 3.141 * r
    return a
    
def area(r):
    r = r ** 2
    a = 2 * 3.141 * r 
    return a
    
    
def main():
    print(circumference(5))
    print(area(5))
    
if __name__ == "__main__":
    main()