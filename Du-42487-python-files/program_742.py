
def reverse_list(a):
	b=[]
	i=0
	while i < len(a):
		b.append(a.pop())
	i=i+1
	return b

def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()