import sys

def reverse_list(l):
	if len(l) == 0:
		return []

	return reverse_list(l[-1]).append(l[:-1])