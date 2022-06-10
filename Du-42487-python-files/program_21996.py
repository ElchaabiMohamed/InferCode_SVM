def selection_sort(a):
	
	
	c=0
	while c<len(a):
		i= c
		p=c	
		while i<len(a):	
			if a[p]<a[i]:
				p=i
			z=a[p]
			a[p]=a[c]
			a[c]=z
			i+=1
		
		c+=1
