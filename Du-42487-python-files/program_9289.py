def swap_keys_values(d):
	dic={}
	a=list(d.values())
	b=list(d.keys())
	for i in range(0,len(a)):
		dic[a[i]]=b[i]
	return dic
