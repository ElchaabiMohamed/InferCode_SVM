import sys
def swap_keys_values(d):
	new_dict={}
	for (z,q) in (list(d.items())):
		new_dict[q]=z
	return(list(new_dict.items()))


	
