import sys
def swap_keys_values(d):
	new={}
	for (z,q) in (list(d.items())):
		new[q]=z
	return(list(new.items()))


	
