def reverse_list(a):
	if len(a) == 1 or len(a) == 0:
		return a
	cancer = reverse_list(a[1:])
	cancer.append(a[0])
	return cancer