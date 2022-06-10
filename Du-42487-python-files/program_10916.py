#!/usr/bin/env Python

# Your function definition goes here.
pi = 3.141

def area(n):
	area = pi * (n ** 2)
	return area

def circumference(n):
	circumference = 2 * pi * n 
	return circumference
	
def main():
	circumference(3)
	
if __name__ == "__main__":
	main()