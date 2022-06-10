pi = 3.141
def circumference(r):
	cir = (2 * pi) * r
	return cir

def area(r):
	area = pi * (r ** 2)
	return area 

def main():
   print(area(7))
   print(circumference(5))

if __name__ == "__main__":
   main()