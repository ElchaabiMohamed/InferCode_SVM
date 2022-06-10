pi = 3.141

def circumference(x):
	return (float(x) * 2 * pi)

def area(x):
	return (float(x) ** 2) * pi

def main():
	print(circumference(0.5))
	print(area(3))

if __name__ == "__main__":
	main()