import sys

def swap_unique_keys_values(dic):
	a, b, c = [], [], {}
	for file in dic:
		a.append([file, dic[file]])
	for letter in a:
		if letter[1] in c:
			del c[letter[1]]
		else:
			c[letter[1]] = letter[0]
	return c
	
if __name__ == "__main__":
	main()