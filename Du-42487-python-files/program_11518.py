pi = 3.141

def circumference(x):
	return (int(x) * 2 * pi)

def area(x):
	return (int(x) ** 2) * pi

def main():
	print(circumference(2))
	print(area(3))

if __name__ == "__main__":
	main()