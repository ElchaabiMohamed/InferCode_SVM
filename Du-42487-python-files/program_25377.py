pi = 3.141

def circumference(r):
    a = 2 * pi * r
    return a
    
def area(r):
    r = r ** 2
    a = pi * r 
    return a
    
    
def main():
    print(circumference(5))
    print(area(5))
    print(area(0.5))
    
if __name__ == "__main__":
    main()