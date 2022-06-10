import sys #Gellert
def swap_keys_values(dic):
	a, b, c = [],[], {}
	for file in dic:
		a.append(file)
	for letter in a:
		if letter not in c:
			c[dic[letter]]= letter
	return c
	
if __name__ == "__main__":
	main()
