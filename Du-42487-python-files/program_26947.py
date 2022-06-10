import sys

def overlap(x1=0,y1=0,r1=1,x2=0,y2=0,r2=1):
   return (int(r1)-int(r2))**2 <= (int(x1)-int(x2))**2 + (int(y1)-int(y2))**2 < (int(r1)+int(r2))**2

def main():
   
   print((overlap())) 
   
if __name__ == '__main__':
   main()
   