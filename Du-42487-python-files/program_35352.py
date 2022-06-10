import sys
"""
def swap_unique_keys_values(x):
	x1 = {}
	x2 ={}
	sorx = sorted(x.items(),reverse=True)
	for keys,values in sorx:
		if values not in x1:
			x1[values] = keys
		else:
			x1[values] = "N"
	sorx2 = sorted(x1.items(), reverse=True)
	for keys,values in sorx2:
		if values != sorx2:
			x2[keys] = values
	return x2
"""

def swap_unique_keys_values(x):
	x1 = {}
	x2 = {}
	sorx = sorted(list(x.items()),reverse = True)
	for keys, values in sorx:
		if values not in x1:
			x1[values] = keys
		else: 
			x1[values] = "N"
	sorx2 = sorted(list(x1.items()), reverse= True)
	for keys,values in sorx2:
		if values != "N":
			x2[keys] = values
	return x2