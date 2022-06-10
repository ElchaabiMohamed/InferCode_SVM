pi = 3.141

def circle_circumference(r):
	c = 2 * pi * r
	return c

def circle_area(r):
   a = pi * r **2
   return a

def main():
   print(circle_circumference(2))
   print(circle_area(3))

if __name__ == "__main__":
   main()