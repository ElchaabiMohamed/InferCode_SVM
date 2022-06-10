import sys

def reverse_list(l):
	if len(l) == 0:
		return []

	return l[-1].append(reverse_list(l[1:]))