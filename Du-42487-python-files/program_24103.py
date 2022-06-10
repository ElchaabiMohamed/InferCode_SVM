def square_area(m):
   return m * m

def square_perimeter(l):
   return 4 * l

def circle_area(a):
   return 3.14 * a**2

def circle_circumference(b):
   return 2 * 3.14 * b

def rectangle_perimeter(c):
   return (c + c) * 2

if __name__ == "__main__":
   print(square_area(2))
   print(square_perimeter(2))
   print(circle_area(2))
   print(circle_circumference(3))
   print(rectangle_perimeter(4))

