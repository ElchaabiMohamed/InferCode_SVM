import sys
d = {"a" : 4 , "b" : 7, "c" : 10} 
d2 = {v:k for k, v in list(d.items())}

def swap_keys_values(dict):
	new_dict = {v:k for k, v in list(dict.items())}
	print ([new_dict])
	
swap_keys_values(d)