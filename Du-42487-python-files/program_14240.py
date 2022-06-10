def square_area(x1,y1,x2,y2):
   dx = x1 - x2
   dy = y1 - y2
   area = dx * dy
   if 0 <= area:
      return area
   else:
      return -area

if __name__ == "__main__":
   # We are being executed directly, so run some tests.
     print(square_area(2,3,4,5))
