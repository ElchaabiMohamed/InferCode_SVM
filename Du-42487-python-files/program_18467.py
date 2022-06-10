# Calculate the area of a circle.
def circle_area(r):
   return r * r * 3.141

# Calculate the area of a rectangle.
def rectangle_area(x1,y1,x2,y2):
   dx = x1 - x2
   dy = y1 - y2
   area = dx * dy
   if 0 <= area:
      return area
   else:
      return -area
      
def square_area(x, y):
    area = x * y
    if 0 <= area:
        return area
    else:
        return -area
      
def square_perimeter(x):
    return x * 4
    
def circle_circumference(r):
    return 2 * 3.14 * r
    
def rectangle_perimeter(x, y):
    return (2 * x) + (2  * y) 
    
# When executed directly as a Python script, __name__ will be "__main__".
# When imported, __name__ will be "geometry".

if __name__ == "__main__":
   # We are being executed directly, so run some tests.
   print(circle_area(2))
   print(rectangle_area(2,3,4,5))
