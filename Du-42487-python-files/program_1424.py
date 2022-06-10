def minimum(l):
	try:
		if l[0] < l[1]:
			return minimum(l[:1] + l[2:])
		else:
			return minimum(l[1:])
	except IndexError:
		return l[0]

print((minimum([6,5,1,3,4])))