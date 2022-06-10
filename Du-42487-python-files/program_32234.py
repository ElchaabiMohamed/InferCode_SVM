def bsearch(a, q):
	low = 0
	high = len(a)
	while low != high:
		mid = (low + high) / 2

		if a[mid] < q:
			low = mid + 1
		else:
			high = mid

	return low

li = [2, 2, 4, 4, 7, 10, 10, 11, 20, 25, 25]
num = 2

if __name__ == "__main__":
	print(bsearch(li, num))
