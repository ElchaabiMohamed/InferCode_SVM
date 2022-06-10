#!usr/bin/env python

def circumference(r):
	return 2 * 3.141 * r

def area(r):
	return 3.141 * (r ** 2)

def main():
	print(circumference(5))
	print(area(6))

if __name__ == "__main__":
   main()