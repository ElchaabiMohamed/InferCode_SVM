def bsearch(a, q):
	low = 0
	high = len(a)
	while low != high:
		mid = (low + high) / 2

		if a[mid] < q:
			low = mid + 1
		else:
			high = mid

	print(low)

li = [1, 2, 3, 5, 6, 7]
num = 5

if __name__ == "__main__":
	bsearch(li, num)
