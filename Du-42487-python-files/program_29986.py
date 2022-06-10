#!usr bin/env python

def overlap(x1=0,y1=0,r1=1,x2=0,y2=0,r2=1):
   try:
      return ((((int(x2) - int(x1)) ** 2) + ((int(y2) - int(y1)) ** 2)) ** -1)
   except ZeroDivisionError:
      return True

def main():
   ol = overlap(())
   print(ol)

if __name__ == '__main__':
   main()
