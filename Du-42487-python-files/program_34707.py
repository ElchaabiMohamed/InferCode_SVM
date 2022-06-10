
def swap_key_values(d):
	new_dict = dict(list(zip(list(d.values()), list(d.keys()))))
	return new_dict