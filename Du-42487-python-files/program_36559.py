#Explanation: l2 = [] always points to a certain point in memory, the list [].
#l1's list contents are then appended to it, editing it directly.
#l2 = [] always points to the same point in memory, even when it is edited.
 
 
#To solve this we simply create a new list, and make sure l2 is never directly edited.
#ps. id(object) shows the memory point.

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
