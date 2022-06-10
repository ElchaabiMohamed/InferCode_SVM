import random

def unique(data):
	previous = []
	new = []
	for integer in data:
		if integer not in new and integer not in previous:
			new.append(integer)
		elif integer not in new and integer in previous:
			continue
		elif integer in new and integer not in previous:
			previous.append(integer)
			new.remove(integer)
	return new
			
	
def swap_unique_keys_values(d):
	values = [n for n in list(d.values())]
	special = unique(values)
	return {v : k for (k, v) in list(d.items()) if v in special}
		
