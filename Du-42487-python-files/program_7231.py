import sys

def swap_unique_keys_values(dick):
	newdick = {}
	for (k,v) in list(dick.items()):
		if v not in newdick:
			newdick[v] = k
	return newdick







if __name__ == '__main__':
	main()