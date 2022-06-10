
def reverse_list(a, new_a=None):
	if new_a == None:
		new_a = []
	if len(a) > 0:
		new_a.append(a.pop())
		return reverse_list(a, new_a)
	else:
		return new_a