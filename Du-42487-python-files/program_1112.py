def pi(pi):
	return 3.141
def circumference(r):
	return float(2*r*pi)
def area(r):
	return float(pi*r**2)



def main():
	print(circumference(4))
	print(area(4))

if __name__=="__main__":
	main()