def minimum(s):
	if len(s) == 1:
		return s[0]
	else:
		min_ret = minimum(s[1:])
		return s[0] if s[0] < min_ret else min_ret


