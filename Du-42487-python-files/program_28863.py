def minimum(lst):
	if lst == []:
		return 0
	return 1 + minimum(lst[:-1])

if __name__ == "__main__":
	print((minimum((["", "", "", "", "", "", ""]))))