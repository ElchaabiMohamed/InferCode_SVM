import sys
def overlap(x1 = 0, y1 = 0, r1 = 1, x2= 0, y2= 0, r2 = 1):
	if ((x2 - x1)**2 + (y2 - y1)**2)**1/2 < r1 + r2:
		return "True"
	else:
		return "False"
def main():
	pass
if __name__ == "__main__":
	main()