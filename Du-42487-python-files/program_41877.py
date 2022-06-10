pi = 3.141

def circumference(r):
   s = 2 * pi * r
   return s

def area(r):
   t = pi * r ** 2
   return t

def main():
   print(circumference(2))
   print(area(3))

if __name__ == "__main__":
   main()
