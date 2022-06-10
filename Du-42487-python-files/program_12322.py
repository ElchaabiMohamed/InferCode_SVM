def get_price(age):

 	if int(age) <= 16:
 	  return '5' 
 	elif int(age) > 60:
 	  return '7'
 	else:
 	  return '10'


def merge_lists(l1,l2):
		newlist = []
		i = 0
		while i < len(l1):
			newlist.append(l1[i])
			i = i + 2

		j = 0
		while j < len(l2):
			newlist.append(l2[j])
			j = j + 2
		return newlist

def weird_case(lines):
	lines = lines.upper().split()


	a = lines[0]
	b = lines[1]
	c = lines[2]
	a1 = ""
	b2 = ""
	c3 = ""

	i = 0
	while i < len(a):
		if i % 2 == 0:
			a1 +=  a[i]
		else:
			a1 += a[i].lower()
		i = i + 1
	i = 0
	while i < len(b):
		if i % 2 == 0:
			b2 +=  b[i]
		else:
			b2 += b[i].lower()
		i = i + 1
	i = 0
	while i < len(c):
		if i % 2 != 0:
			c3 +=  c[i]
		else:
			c3 += c[i].lower()
		i = i + 1

	return a1 + " " + b2 + " " + c3

def remove_zeros(x):
	i = 0
	while i < len(x):
		if x[i] == 0:
			del x[i]
		if x[i] == 0:
			del x[i]
		i = i + 1
	return x
