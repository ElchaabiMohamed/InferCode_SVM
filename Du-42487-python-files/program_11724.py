

def minimum(l):
	if len(l) == 1:
		return l
	else:
		return mini(l[0], minimum(l[1:]))


