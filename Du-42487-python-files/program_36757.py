import sys
def swap_unique_keys_values(d):
	store={}
	di=d
	for key in d:
		for k in di:
			if key ==k:
				break
			if di[k]==d[key]:
				continue
			else:
				store[key]=d[k]
	return({v:k for (v,k) in list(store.items())})

if __name__ =='__swap_unique_keys_values__':
	print((swap_unique_keys_values()))