import sys
def swap_unique_keys_values(d):
	dic1 = {}
	dic2 = {}
	dicsort = sorted(list(d.items()), reverse = True)
	for k , v in dicsort:
		if v not in dic1:
			dic1[v] = k
		else:
			dic1[v] = "N"
	dicsort2 = sorted(list(dic1.items()), reverse = True)
	for k , v in dicsort2:
		if v != "N":
			dic2[k] = v
	return dic2


if __name__ == '__main__':
	main()


