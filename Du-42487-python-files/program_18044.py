def power(n, i):
	if i == 0:
		return 1
	return n * power(n, i-1)

from sys import argv
if __name__ == "__main__":
	print((power((int(argv[1])), int(argv[2]))))