def maximum(lst):
	if len(lst) == 1:
		return lst[0]
	if lst[0] < lst[-1]:
		return maximum(lst[1:])
	if lst[0] > lst[-1]:
		return maximum(lst[:-1])

if __name__ == "__main__":
	print((maximum((list(range(10, 0, -1))))))