def circumference(r):
	cir = (2 * 3.141) * r
	return cir

def area(r):
	area = 3.141 * (r ** 2)
	return area 

def main():
   print(area(7))
   print(circumference(5))

if __name__ == "__main__":
   main()