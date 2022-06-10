#!/usr/bin/env python
pi = 3.141

def circumference(r):
	return r * 2 * pi

def area(r):
	return 3 * pi * r

def main():
	print(circumference(2))
	print(area(3))

if __name__ == "__main__":
	main()