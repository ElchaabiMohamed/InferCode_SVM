def minimum(s):
	if s == 1:
		return s[0]
	else:
		min = minimum(s[1:],s-1)
		if s[0] < min:
			return s[0]
		else:
			return min
