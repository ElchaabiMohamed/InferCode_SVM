def reverse_list(s):
	if len(s) == 1:
		return s
	else:
		return s[-1] + reverse_list[:-1] 

