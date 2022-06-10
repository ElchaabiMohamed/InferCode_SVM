#!usr/bin/env python

# finds the circumference of a circle radius 'r'.
def circumference(r):
	return 2 * r * 3.141


#finds the area of a circle radius 'r' 
def area(r):
	return 3.141 * (r ** 2)


def main():
   print(circumference(5))
   print(area(2))

if __name__ == "__main__":
   main()