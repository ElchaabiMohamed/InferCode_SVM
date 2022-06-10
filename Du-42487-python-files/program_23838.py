import sys

def overlap(x1, y1, r1, x2, y2, r2):
   distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 1 // 2
   return distance < r1 + r2

def main():
   print((overlap(10,0,1,8,0,1)))
   


if __name__ == '__main__':
   main()
