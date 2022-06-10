pi=3.141

def circumference(r):
   c=2*pi*r
   return c

def area(r):
   a=pi*r*r
   return a
   
def main():
   print(circumference(5))
   print(area(5))

if __name__ == "__main__":
   main()
   