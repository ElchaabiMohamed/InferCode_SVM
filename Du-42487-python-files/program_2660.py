def swap(a,i,j):
	tmp = i
	i = j
	j = tmp
	return a
	

i = 0
j = (len(a) - 1)
def reverse(a):
	while i < j:
		swap(a,i,j)
		i = i + 1
		j = j - 1
		
