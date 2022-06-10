import sys

def swap_unique_keys_values(x):
	sorx = sorted(d.items,reverse=True)
	x1 = {}
	x2 ={}
	for keys,values in sorx:
		if v not in x1:
			x1[values] = keys
		else:
			x1[v] = "N"
	sorx2= sorted(list(x1.items()), revers=True)
	for keys,values in sorx2:
		if v != sorx2:
			x2[keys] = values
	return x2