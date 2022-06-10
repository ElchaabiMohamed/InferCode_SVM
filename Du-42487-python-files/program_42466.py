import sys #Gellert
def swap_unique_keys_values(dic):
	a, b, c = [],[], {}
	for file in dic:
		if file in a:			
			a.pop(a.index(dic[file]))
		else:
			a.append([file, dic[file]])
		#print (a)
	for letter in a:
		#	print (letter)
			if letter[1] in c:
				del c[letter[1]]
			else:
				c[letter[1]]= letter[0]
	#print (c)
	return c
	
if __name__ == "__main__":
	main()
