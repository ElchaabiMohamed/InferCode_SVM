#!/usr/bin/env python3

def overlap(x1=0,y1=0, r1=1, x2=0,y2=0, r2=1):
   h = y2 - y1
   b = x2 - x1
   hyp = (h**2)+(b**2)**(1/2)
   return not (r1 + r2) <= hyp
      

def main():
   pass

if __name__ == '__main__':
    main()

