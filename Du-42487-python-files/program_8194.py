import sys

def swap_unique_keys_values(d):
	swap1 = {}
	swap2 = {}
	swapsorted1 = sorted(list(d.items()), reverse = True)
	for k,v in swapsorted1:
		if v not in swap1:
			swap1[v] = k
		else:
			swap1[v] = "N"
	swapsorted2 = sorted(list(swap1.items()), reverse = True)
	for k,v in ar2:
		if v != "N":
			swap2[k] = v
	return swap2