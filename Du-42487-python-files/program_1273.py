pi = 3.141
def circumference(r):
   return 2*pi*int(r)

def area(r):
   return pi*int(r)*int(r)

def main():
   print(circumference(2))
   print(area(3))
   
if __name__ == "__main__":
   main()
