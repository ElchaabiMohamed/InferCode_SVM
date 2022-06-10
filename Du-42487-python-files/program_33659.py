#!usr bin/env python

def overlap(x1=0,y1=0,r1=1,x2=0,y2=0,r2=1):
   if (((int(x2) - int(x1)) ** 2) + ((int(y2) - int(y1)) ** 2)) != 0:
      return ((((int(x2) - int(x1)) ** 2) + ((int(y2) - int(y1)) ** 2)) ** -1) < int(r1) + int(r2)


def main():
   ol = overlap(())
   print(ol)

if __name__ == '__main__':
   main()
