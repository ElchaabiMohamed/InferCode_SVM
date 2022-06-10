def swap(a,i,j):
	b=a
	tmp = b[j]
	b[j] = b[i]
	b[i] = tmp

i=0


def reverse(a):
	c=a
	while i < len(a):
		swap(c,c[i],c[len(c)-i-1])
		i=i+1
	return c
		





