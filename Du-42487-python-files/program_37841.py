def reverse_list(lst):
	if lst == []:
		return []
	return [lst[-1]] + reverse_list(lst[:-1])

if __name__ == "__main__":
	print((reverse_list(list(range(10)))))