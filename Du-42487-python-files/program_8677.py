pi=3.141
def circumference(x):
	x=2*x*pi
	return x
def area(x):
	x=pi*(x**2)
	return x
def main():
   print(circumference(2))
   print(area(3))

if __name__ == "__main__":
   main()