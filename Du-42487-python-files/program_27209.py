def func_selection_sort(a):
	i=0
	j=0
	p=0
	while i<len(a):
		j=i+1
		p=i
		while j<len(a):
			if a[p] > a[j] :
				p=j
			j=j+1

		tmp=a[i]
		a[i]=a[p]
		a[p]=tmp
		i=i+1
	return a


def main():
	a=[1,4,6,3,4,5]
	
	print(func_selection_sort(a))

if __name__ == "__main__":
   main()