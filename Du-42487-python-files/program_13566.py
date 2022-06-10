def selection_sort(a):
	i = 0
	while i < len(a):
		j = i + 1
		while j < len(a):
			if a[j] < a[i]:
				tmp = a[j]
				a[j] = a[i]
				a[i] = tmp
			j += 1
		i += 1
	return a


def main():
	a = [1, 4, 7, 77, 2, 54532, 1, 0]
	print(selesction_sort(a))

if __name__ == "__main__":
	main()