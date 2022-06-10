import sys


def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
	run = int(x1) - int(x2)
	rise = int(y1) - int(y2)
	distance = ((run ** 2) + (rise ** 2)) ** (0.5)

	return distance < (r1 + r2)

def main():
	print((overlap()))
	print((overlap(10)))
	print((overlap(10, 10)))
	print((overlap(10, 10, 10)))
	print((overlap(10, 0, 10)))
	print((overlap(10, 0, 1, 8, 0, 1)))
	print((overlap(10, 0, 1, 8, 0, 2)))


if __name__ == '__main__':
	main()
