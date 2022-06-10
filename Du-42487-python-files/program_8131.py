def maximum(s):
	if len(s) == 1:
		return s[0]
	else:
		maxi =maximum(s[1:])
		return l[0] if l[0] > maxi else maxi