import sys

def reverse_list(l):
	if l == None:
		return l

	return reverse_list(l[-1]).append(l[:-1])