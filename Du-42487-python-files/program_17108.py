import sys


def overlap(xo=0, yo=0, ro=1, xt=0, yt=0, rt=1):
	run = int(xo) - int(xt)
	print(run)
	rise = int(yo) - int(yt)
	print(rise)
	distance = ((run ** 2) + (rise ** 2)) ** (0.5)
	print(distance)

	return distance < (ro + rt)

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