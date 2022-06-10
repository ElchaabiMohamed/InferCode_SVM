import sys

def reverse_list(l):
	if l == []:
		return []
	elif len(l) == 1:
		return l	
	else:
		return reverse_list(l[-1:]).append(l[0])