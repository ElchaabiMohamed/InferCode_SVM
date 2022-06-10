def append2list(l1, l2=[]):
	for i in l1:
		l2.append(i)
	if len(l2) < 2:
		return l2
	else:
		l2.remove(l2[0])
		l2.remove(l2[0])
		return l2

def main():
	list1 = ["cat", "dog"]
	nlist = append2list(list1)
	print(nlist)


if __name__ == '__main__':
    main()