pi = 3.141
def circumference(n):
	return 2 *pi * n

def area(n):
	return pi * (n ** 2)

def main():
   print(circumference(2))
   print(area(3))

if __name__ == "__main__":
   main()