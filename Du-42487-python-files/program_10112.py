def bsearch(a, q):
	start = 0
	end = len(a)

	while end > start:
		m = (start + end) / 2
		if a[m] < q:
			start = m + 1
		else:
			end = m
	return start

if __name__ == '__main__':
	print(bsearch([2, 3, 6, 6, 7, 8], 4))

