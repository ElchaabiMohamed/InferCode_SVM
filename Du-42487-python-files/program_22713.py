def swap(a,i,j):
	# Swap the items at index i and j in the list a 
	a[i], a[j] = a[j], a[i]
	
def find_position_of_smallest(a,i):
	# Find the position of the smallest item in list a
	# Starting from index i to the end of the list 
	smallest = a[i] 
	for j in a[i:]:
		if a[j] < smallest:
			smallest = j
	return smallest 