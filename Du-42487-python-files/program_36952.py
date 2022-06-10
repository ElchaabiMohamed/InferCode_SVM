pi = 3.141

def circle_circumference(r):
	c = 2 * pi * r
	return c

def circle_area(r):
   a = pi * r **2
   return a

def main():
   print(circle_circumference(r))
   print(circle_area(r))

if __name__ == "__main__":
   main()