def reverse_list(s):
	if len(s) == 0:
		return[]
	else:
		return [s[-1]] + reverse_list(s[:-1])
