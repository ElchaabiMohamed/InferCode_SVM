#!/usr/bin/env python

def square_area(side):
   sq = side * side
   return sq

def square_perimeter(side):
   perimeter = side * 4
   return perimeter

def circle_area(radius):
   area = 3.14 * radius ** 2
   return area

def circle_circumference(radius):
   circumference = 2 * 3.14 * radius
   return circumference

def rectangle_perimeter(length, width):
   perimeter = (length * 2) + (width * 2)
   return perimeter 
