import sys

def swap_keys_values():
	{v:k for k, v in list(sys.argv[1].items())}