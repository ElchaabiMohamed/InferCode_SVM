def square_area(side):
   return side * side  

def square_perimeter(q):
   return q * 4

def circle_area(r):
   return r * r * 3.14 

def circle_circumference(s):
   return 2 * 3.14 * s

def rectangle_perimeter(l,w):
   return 2 * l + 2 * w

if __name__ == "__main__":
     print(square_perimeter(2)) 
     print(circle_area(2)) 
     print(circle_circumference(3)) 
     print(rectangle_perimeter(2,4)) 
