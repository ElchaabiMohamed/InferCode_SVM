def reverse_list(input_list, workinglist=[], new=True):
	if new:
		workinglist = []
	if len(input_list) == 0:
		return workinglist
	else:
		workinglist.append(input_list[-1])
		return reverse_list(input_list[:-1], workinglist, False)



def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()