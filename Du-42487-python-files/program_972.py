def count(n):
	if n == "":
		return 0
	return 1 + count(n[1:]) 