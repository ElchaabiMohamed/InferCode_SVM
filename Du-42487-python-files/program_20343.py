

pi = 3.141

def circumference(r):
	y = 2*pi*r
	return y
def area(r):
	area = pi*(r**2)
	return area

def main():
	print(circumference(5))
	print(area(5))

if __name__ == '__main__':
	main()


