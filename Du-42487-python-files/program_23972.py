def reverse_list(s):
	if len(s) == 1 or len(s) == 0:
		return s
	else:
		return s[-1] + reverse_list(s[:-1]) 

