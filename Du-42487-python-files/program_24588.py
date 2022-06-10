
def reverse_list(l, new_list=None):
	if new_list == None:
		new_list = []
	if len(l) > 0:
		new_list.append(l.pop())
		return reverse_list(l, new_list)
	else:
		return new_list