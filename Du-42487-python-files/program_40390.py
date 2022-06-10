#!usr/bin/env python

# finds the circumference of a circle radius 'r'.
def circumference(r):
	return 2 * r * pi


#finds the area of a circle radius 'r' 
def area(r):
	return pi * (r ** 2)


def main():
   print(circumference(5))
   print(area(2))

pi = 3.141

if __name__ == "__main__":
   main()