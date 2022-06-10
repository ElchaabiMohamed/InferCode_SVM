import sys
def swap_unique_keys_values(d):
	keys = []
	values = []
	unique = []
	swapped_unique_d = {}
	for key in d:
		keys.append(key)
		values.append(d[key])

	for item in keys:
		unique.append(True)

	i = 0 
	while i < len(keys):
		p = i + 1
		while p < len(values):
			if values[i] == values[p]:
				unique[i] = False
				unique[p] = False
			p += 1
		i += 1
	j = 0
	while j < len(unique):
		if unique[j]:
			swapped_unique_d[values[j]] = keys[j]
		j += 1
	return(swapped_unique_d)

def main():
	a_dict = {"a" : 1, "b" : 2, "c" : 1, "d" : 7, "e" : 2, "f" : 4}
	print((swap_unique_values(a_dict)))

if __name__ == "__main__":
	main()