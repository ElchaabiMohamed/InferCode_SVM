#!/usr/bin/env python


def circumference(r):
	pi = 3.141
	return 2 * pi * r

def area(r):
	pi = 3.141
	return pi * r ** 2

def main():
	print(circumference(2))
	print(area(3))

if __name__ == "__main__":
	main()