#!/usr/bin/env python

def walkback(a, q, i):
	while i > 1 and a[i-1] == q:
		i -= 1

	return i


def bsearch(a, q):
	low = 0
	high = len(a)

	while low < high:
		guess = low + (high - low) // 2
		# print "guessing...", guess, "found", a[guess]

		if a[guess] == q:
			return walkback(a, q, guess)
		elif a[guess] < q:
			low = guess + 1
		else:
			high = guess

	return low

if __name__ == "__main__":
	print(bsearch([2,3,6,6,7,8], 1) == 0)
	print(bsearch([2,3,6,6,7,8], 2) == 0)
	print(bsearch([2,3,6,6,7,8], 4) == 2)
	print(bsearch([2,3,6,6,7,8], 6) == 2)
	print(bsearch([2,3,6,6,7,8], 8) == 5)
	print(bsearch([2,3,6,6,7,8], 9) == 6)
	print(bsearch([2, 2, 4, 4, 7, 10, 10, 11, 20, 25, 25], 3))