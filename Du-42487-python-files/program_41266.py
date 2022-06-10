def reverse_list(s, x =[]):
	if len(s) == 1 or len(s) == 0:
		return s
	else:
		x.append(s[-1])
		return x + reverse_list(s[:-1], x) 

