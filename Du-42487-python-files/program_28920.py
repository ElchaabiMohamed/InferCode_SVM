def get_odd_list():
	odd = []
	num = eval(input())
	while num != -1:
		if num % 2 == 1:
			odd.append(num)
			num = eval(input())
	return odd

def get_even_oddlist():
	odd = []
	even = []
	num = eval(input())
	while num != -1:
		if num % 2 == 1:
			odd.append(num)
			num = eval(input())
		else:
			even.append(num)
			num = eval(input())
	return (odd,even)

def get_sliced_lists(lst):
	return (lst[:-1],lst[1:-1],lst[::-1])

def get_counts(words):
	words = sorted(words,key=len)
	return words

def main():
	lst = ["dog", "pest", "horse", "donkey", "a", "dolphin", "elephant", "fisherman"]
	print((get_counts(lst)))

if __name__ == "__main__":
	main()