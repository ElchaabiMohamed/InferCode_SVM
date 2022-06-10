def selection_sort(a):
	i = 0
	while i < len(a):
		j = i
		smallest = j
		while j < len(a):
			if a[j] < a[smallest]:
				smallest = j
			j = j + 1
		a[i], a[smallest] = a[smallest], a[i]
		i = i + 1
	return a
		
def main():
	print(selection_sort([1, 2, 3, 1, 2, 3]))
   
if __name__ == "__main__":
   main()