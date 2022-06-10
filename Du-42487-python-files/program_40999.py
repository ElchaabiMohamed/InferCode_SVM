def selection_sort(a):
	i = 0
	j = 1
	while j < len(a):
		if a[j] < a[i]:
			tmp = a[j]
			a[j] = a[i]
			a[i] = tmp
			if i != 0:
				i -= 1
				j -= 1
		else:
			i += 1
			j += 1

def main():
	print(a)
	selection_sort(a)
	print(a)

if __name__ == "__main__":
	main()