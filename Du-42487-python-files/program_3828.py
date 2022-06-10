pi = 3.141
def area(r):
	y = pi * r * r
	return y

def circumference(r):
	y = 2 * pi * r
	return y

def main():
   print(area(3))
   print(circumference(2))

if __name__ == "__main__":
   main()