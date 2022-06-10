import sys

def swap_unique_keys_values(d):
	new_d = {}
	vv = []
	for k in d:
		vv.append(d[k])
	for num in vv:
		for k in d:
			if not vv.count(num) > 1:
				if d[k] == num:
					new_d[num] = k

	return new_d
			

