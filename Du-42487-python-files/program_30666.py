import sys

def reverse_list(l):
	if len(l) == 1:
		return l[0]
	

	return reverse_list(l[-1]).append(l[:-1])