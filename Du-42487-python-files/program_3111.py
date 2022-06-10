import sys

# d = {"a" : 4,
# 		"b" : 7,
# 		"c" : 10,
# 		"d" : 7,
# 		"e" : 6}	

def swap_unique_keys_values(d):
	oldvalues = [v for v in list(d.values())]
	oldkeys = [k for k in list(d.keys())]
	counts = {}
	for v in oldvalues:
		if v not in counts:
			counts[v] = 1
		else:
			counts[v] += 1
	unique = []
	for v in counts:
		if counts[v] == 1:
			unique.append(v)
	reverseddic = {}
	for i in range(0, len(oldvalues)):
		reverseddic[oldvalues[i]] = oldkeys[i]
	newdic = {}
	for (k,v) in list(reverseddic.items()):
		if k in unique:
			newdic[k] = v
	return newdic

# if __name__ == '__main__':
# 	main()