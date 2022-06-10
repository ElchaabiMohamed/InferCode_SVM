import random

def swap_keys_values(dictionary):
	dictionary = {v : k for (k, v) in list(dictionary.items())}
	return dictionary

