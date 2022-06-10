def get_odd_list():
	odd = []
	num = input()
	while num != -1:
		if num % 2 == 1:
			odd.append(num)
			num = input()
	return odd

def get_even_oddlist():
	odd = []
	even = []
	num = input()
	while num != -1:
		if num % 2 == 1:
			odd.append(num)
			num = input()
		else:
			even.append(num)
			num = input()
	return (odd,even)

def get_sliced_lists(lst):
	return (lst[:-1],lst[1:-1],lst[::-1])

def get_counts(words):
	

def main():
	pass

if __name__ == "__main__":
	main()