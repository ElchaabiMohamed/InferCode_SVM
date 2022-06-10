def square_area(side):
    return side * side
     
 
def square_perimeter(side):
    return 4 * side
     
 
def circle_area(r):
    return  r * r * 3.14
     
 
def circle_circumference(r):
    return r * 2 * 3.14
     
 
def rectangle_perimeter(l, w):
    return 2 * (l + w)
    
 
if __name__ == "__main__":
   print(square_perimeter(2))
   print(circle_area(2))
   print(circle_circumference(3))
   print(rectangle_perimeter(2 , 4))
