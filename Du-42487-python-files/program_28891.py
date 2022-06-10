def appedn2list(l1,l2 = []):
	return l2 + l1

def main():
	list1 = ["cat", "dog"]
	nlist = appedn2list(list1)
	print(nlist)

	lsit2 = ["lion"]
	nlist = appedn2list(lsit2 , ["antelope"])
	print(nlist)

	list3 = ["fox", "chicken"]
	nlist = append2list(list3)
	print(nlist)

if __name__ == '__main__':
	main()	
