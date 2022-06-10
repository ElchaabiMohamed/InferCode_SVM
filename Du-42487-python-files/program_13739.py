pi = 3.141
def circumference(r):
	c = 2 * pi * r
	return c

def area(r):
	a = pi * r ** 2 
	return a

def main():
	print(circumference(3))
	print(area(2))

if __name__ == "__main__":
	main()