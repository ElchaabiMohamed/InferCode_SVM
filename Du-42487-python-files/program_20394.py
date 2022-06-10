def minimum(l, i=0):
	j=i
	while j<len(l) and l[j]>l[-1]:
		j+=1
		#print (l[j])
	if j<len(l):
		#print (l[j], l[i])
		tmp = l[i]
		l[i] = l[j]
		l[j] = tmp
		#print (l)
	if j>len(l):
		return l[0]
	return minimum(l, i+1)
