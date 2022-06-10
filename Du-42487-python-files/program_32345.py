pi = 3.141

def circle_circumference(r):
	c = 2 * pi * r
	return c

def circle_area(x):
   a = pi * x **2
   return a

def main():
   print(circle_circumference())
   print(circle_area())

if __name__ == "__main__":
   main()