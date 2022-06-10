def maximum(s):
	if len(s) == 1:
		return s[0]
	else:
		maxi =maximum(s[1:])
		return s[0] if s[0] > maxi else maxi