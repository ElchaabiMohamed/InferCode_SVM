def square_area(n):
   square_area = n*n
   return square_area

def square_perimeter(n):
   square_perimeter = n*4
   return square_perimeter

def circle_area(r):
   circle_area = r * r * 3.14
   return circle_area 

def circle_circumference(r):
   circle_circumference = 2*3.14*r
   return circle_circumference

def rectangle_perimeter(x1,y1,x2,y2):
   dx = x1 - x2
   dy = y1 - y2
   area = dx * dy
   if 0 <= area:
      return area

