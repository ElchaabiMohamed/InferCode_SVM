import sys
def swap_unique_keys_values(d):
	new_dict={}
	seen=[]
	for (z,q) in (list(d.items())):
		if q not in seen  :		
			new_dict[q]=z
		seen.append(q)
	return(new_dict)


	
