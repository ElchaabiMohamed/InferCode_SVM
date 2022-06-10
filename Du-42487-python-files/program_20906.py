
def selection_sort(a):
	i = 0
	while i < len(a):
		j = i + 1
		minimum = i

		while j < len(a):
			if a[j] < a[minimum]:
				minimum = j
			j += 1

		tmp = a[minimum]
		a[minimum] = a[i]
		a[i] = tmp

		i += 1
	return a


def main():
	a = [1, 2, 3, 1, 2, 3]
	print(selection_sort(a))

if __name__ == "__main__":
	main()