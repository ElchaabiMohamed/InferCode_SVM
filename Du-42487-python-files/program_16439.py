import sys
from operator import itemgetter
from copy import deepcopy
d = {"a" : 4 , "b" : 7, "c" : 10} 


def swap_keys_values(dict):
	l = []
	new_dict = {v:k for k, v in list(dict.items())}
	#print ([new_dict])
	#print(new_dict[4])
	new_dict1 = new_dict.copy()
	for k in new_dict1:
		l.append("({}, '{}')".format(int(k), new_dict1[k]))
	print(("[" + ", ".join(sorted(l, key = itemgetter(-3))) + "]"))
	
	#print(new_dict[4])	
#swap_keys_values(d)