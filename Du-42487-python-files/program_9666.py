#!/usr/bin/env python
 
pi = 3.141

def circumference(r):
    return 2 * pi * r
 
def area(r):
    return pi * r * r
 
def main():
    print(circumference(3))
    print(area(2))
 
if __name__ == "__main__":
    main()