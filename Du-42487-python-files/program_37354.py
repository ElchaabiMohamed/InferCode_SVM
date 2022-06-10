a = [1, 2, 3, 4]
def swap(a,i,j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp

def find_position_of_smallest(a,i):
	p = i
	j = i
	while j < len(a):
		if a[j] < a[p]:
			p = j
		j = j + 1
	return p
def sort(a):
	i = 0
	while i < len(a):
	   p = i
	   j = i + 1
	   while j < len(a):
	      if a [j] < a[p]:
	         p = j
	      j = j + 1

	   temp = a[p]
	   a[p] = a[i]
	   a[i] = temp

	   i = i + 1

	    

