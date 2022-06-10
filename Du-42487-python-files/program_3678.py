import sys
from math import sqrt
def overlap(x1 = 0, y1 = 0, r1 = 1, x2 = 0, y2 = 0, r2 = 1):
   distance = sqrt(
      (
         x2 -x1 
      ) **2 
      + (
         y2 - y1
      ) **2
   )

   sumradi = r1 +r2 
   return distance < sumradi
   # if distane < sumradi 
   #     return True
   # elif distance >= sumradi:
   #     return False
   # elif distane == sumradi:
   #     return True

def main():
   print((overlap()))
   print((overlap(10)))
   print((overlap(10,10)))
   print((overlap(10,10,10)))
   print((overlap(10,0,10)))
   print((overlap(10,0,1,8,0,1)))
   print((overlap(10,0,1,8,0,2)))
if __name__ == '__main__':
   main()   
