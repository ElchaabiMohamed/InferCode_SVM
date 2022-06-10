import sys

def swap_key_values():
	new_dict = {v:k for k, v in list(d.items())}
	return new_dict