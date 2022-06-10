import sys

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
	a = int(x1) - int(x2)
	b = int(y1) - int(y2)
	c = ((a ** 2) + (b ** 2)) ** (0.5)
	return c < (r1 + r2)
def main():
	print((overlap()))
	print((overlap(10)))
	print((overlap(10, 10)))
	print((overlap(10, 10, 10)))
	print((overlap(10, 0, 10)))
	print((overlap(10, 0, 1, 8, 0, 1)))
	print((overlap(10, 0, 1, 8, 0, 2)))

main()