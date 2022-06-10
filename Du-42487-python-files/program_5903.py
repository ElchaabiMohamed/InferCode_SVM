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
	a = []
	line = n.strip('\n').split(' ')
	i = 0
	while i < len(line):
		word = line[i]
		x = 0
		while x < len(word):
			a.append(word[x])
			x = x + 1
		a.append(' ')
		i = i + 1

	a.remove(a[len(a)-1])

	print(a)

def remove_zeros(a):
	i = 0
	while len(a):
		if int(a[len(a)-i-1]) == 0:
			a.remove(a[len(a)-i-1])
		i = i + 1