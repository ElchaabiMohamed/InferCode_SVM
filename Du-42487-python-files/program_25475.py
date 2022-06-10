import sys

def overlap(x1 = 0, y1 = 0, r1 = 0, x2 = 0, y2 = 0, r2 = 0):
	if (((y2 - y1) ** 2 + (x2 - x1) ** 2)) < (r1 +r2) ** 2:
		return True
	else:
		return False


if __name__ == '__main__':
    main()
