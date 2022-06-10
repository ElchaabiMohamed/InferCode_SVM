def circumference(r):
   c = (2 * 3.141) * r
   return c

def area(r):
   a = (3.141 * r) ** 2
   return a
   

def main():
   print(circumference(2))
   print(area(3))

if __name__ == "__main__":
   main()