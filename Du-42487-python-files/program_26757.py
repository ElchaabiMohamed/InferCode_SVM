pi=3.141
def circumference(n):
   m=2*pi*n
   return m

def area(n):
   m=pi*(n**2)
   return m
   
def main():
   print(circumference(2))
   print(area(3))

if __name__ == "__main__":
   main()