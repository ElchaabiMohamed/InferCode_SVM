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
		i = i + 1

	i = 0
	while i < len(n):
		if i % 2 == 1 and i != 0:
			n.remove(n[i])
		i = i + 1

	return n

def weird_case(n):
	line = n.strip('\n').split(' ')
	i = 0
	while i < len(line):
		word = line[i]
		x = 0
		while x < len(word):
			return word[x].lower()
			x = x + 1
		i = i + 1