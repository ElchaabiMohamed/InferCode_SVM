def reverse_list(l, i = None):
    if (i is None):
        i = len(l) // 2

    if (i >= 0):
        return reverse_list(l[1:] + [l[0]], i - 1)
    else:
    	return l