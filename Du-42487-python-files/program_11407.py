pi = 3.141

def circumference(r):
    return r * pi * 2
    
def area(r):
    return (r ** 2) * pi
    
def main():
    print(circumference(3))
    print(area(4))
    
if __name__ == "__main__":
    main()