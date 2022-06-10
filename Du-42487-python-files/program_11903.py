def maximum(n):
	if len(n) == 1:
		return n[0]
	else:
		maxim = maximum(n[1:])
		return n[0] if n[0] >maxim else maxim
