import sys
def swap_keys_values(d):
	new_dict={}
	values=[]
	keys=[]
	for (z,q) in (list(d.items())):
		keys.append(q) 
		values.append(z)
	for (z,q) in (list(d.items())):
		if not keys.count(q) > 1 :
			new_dict[q]=z
	return(new_dict)
		
		
 


	
