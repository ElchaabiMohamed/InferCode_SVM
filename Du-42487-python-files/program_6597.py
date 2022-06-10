from math import sqrt

def overlap(x1=0, y1=0, r1=1, x2=1, y2=1, r2=1):
	distance_centre = int(sqrt((x2 - x1)**2 + (y2 - y1)**2))
	distance_radius = r1 + r2
	
	if distance_centre < distance_radius:
		return True
	else:
		return False

def main():
	overlap(x1=0, y1=0, r1=1, x2=1, y2=1, r2=1)

if __name__ == "__main__":
	main()
	


