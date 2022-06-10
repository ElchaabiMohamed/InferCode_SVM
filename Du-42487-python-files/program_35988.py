PI = 3.141

def circumference(r):
	return 2*PI*r

def area(r):
	return PI*r**2

def main():
	print(circumference(2))
	print(area(3))

if __name__ == '__main__':
	main()