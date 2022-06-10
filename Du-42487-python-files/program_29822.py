import sys

def swap_unique_keys_values(d):
	#seen = {}
	#new_d = {}
	#for k in d:
		#seen[k] += 1
	#for item in seen:
		#if d[item] == 1:
			#new_d[item] = True
	#for k in new_d:
		#for key in d:
			#if k in d:
				#new_d[k] = d[key]
	#return new_d
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
			

