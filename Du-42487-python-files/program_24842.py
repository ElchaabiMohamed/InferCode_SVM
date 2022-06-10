a = [0, 1, 2, 3, 4]

def swap(a, i, j):    
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

a = [0, 1, 2, 3]
def find_position_of_smallest(a, i):
	while i < len(a):
	  if a < a[i]:
	    i = 0
	  i = i + 1
	
	

                  
                                
