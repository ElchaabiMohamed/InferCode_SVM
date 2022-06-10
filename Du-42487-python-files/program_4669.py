def selection_sort(a, i):
	p=i
	j = i + 1
	while j<len(a):
		if a[j]<a[p]:
			p=j
		j = j + 1

def main():
	print(selection_sort(a))

if __name__=="__main__":
	main()