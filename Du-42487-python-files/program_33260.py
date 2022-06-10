#!usr/bin/python
pi = 3.141

def circumference(r):
    c = 2 * pi * r
    return c

def area(r):
    a = pi * (r **2)
    return a

if __name__ == "__circumference__":
    circumference(1)

if __name__ == "__area__":
    area(1)