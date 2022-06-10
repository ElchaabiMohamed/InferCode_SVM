pi = 3.141

def circumference(r):
	y = 2 * pi * r
	return y

def area(r):
	y = pi * r * r
	return y

def main():
	print(circumference(5))
	print(area(5))

if __name__ == "__main__":
	main()