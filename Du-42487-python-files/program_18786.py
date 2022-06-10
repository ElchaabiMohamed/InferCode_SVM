pi=3.141

def circumference(r):
	c=r*pi*2
	return c

def area(r):
	a=(r**2)*pi
	return a

def main():
	print(circumference(2)) 
	print(area(3))  

if __name__ == "__main__":
	main()        
