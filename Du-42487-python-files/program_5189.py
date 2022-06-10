import sys

def swap_key_values(d):
	return {v:k for k, v in list(d.items())}