def minimum(lst):
	if len(lst) == 1:
		return lst[0]
	if lst[0] > lst[-1]:
		return minimum(lst[1:])
	if lst[0] < lst[-1]:
		return minimum(lst[:-1])

if __name__ == "__main__":
	print((minimum((list(range(10, 0, -1))))))