#!/usr/bin/env python

def square_perimeter(s):
	return s * 4

def circle_area(r):
	area = r * r * 3.14
	return area

def circle_circumference(r):
	circumference = 2 * 3.14 * r
	return circumference

def rectangle_perimeter(x1,y1,x2,y2):
	perimeter = x1 + y1 + x2 + y2 
	return perimeter


if __name__ == "__main__":
	print(square_perimeter(2))
	print(circle_area(3))
	print(circle_circumference(3))
	print(rectangle_perimeter(1,2,3,4))


