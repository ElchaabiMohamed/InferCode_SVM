import sys
d = {"a" : 4 , "b" : 7, "c" : 10} 
d2 = {v:k for k, v in list(d.items())}

def swap_keys_values(dict):
	l = []
	new_dict = {v:k for k, v in list(dict.items())}
	#print ([new_dict])
	def my_function(a):
		return a[1]
	for k in new_dict:
		l.append("({} : {})".format(k, new_dict[k]))
	print((sorted(l, key = my_function)))
		
	
#swap_keys_values(d)