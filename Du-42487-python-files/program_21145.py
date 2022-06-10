def get_price(n):
	if int(n) <= 16:
		return 5
	elif int(n) > 60:
		return 7
	else:
		return 10

def merge_lists(n, m):
	i = 0
	while i < len(m):
		n.append(m[i])
		m.remove(m[i])
		i = i + 1

	i = 0
	while i < len(n):
		if i % 2 == 0 or i == 0:
			m.append(n[i])
		i = i + 1

	return n
	return m