
def append2list(l1, l2=[]):
	for i in l1:
		l2.append(i)
	l3 = l2
	l2 = []
	return l3

def main():    
	list1 = ['cat', 'dog']
	nlist = append2list(list1)
	# nlist should be ['cat', 'dog']
	print(nlist)
	
	list2 = ['lion']
	list4 = ['antelope']
	nlist = append2list(list2, list4)
	# nlist should be ['antelope', 'lion']
	print(nlist)

	list3 = ['fox', 'chicken']
	nlist = append2list(list3)
	# nlist should be ['fox', 'chicken']
	print(nlist)

if __name__ == '__main__':
	main()
