def swap_keys_values(d):
	new_dict = {v:k for (k, v) in list(d.items())}
	print((sorted(new_dict.items())))
    
