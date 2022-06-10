import sys

def reverse_list(l=None):
	if len(l) == 0:
		return l

	return reverse_list(l[-1]).append(l[:-1])