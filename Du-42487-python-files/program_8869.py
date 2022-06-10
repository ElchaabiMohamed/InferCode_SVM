def swap_unique_keys_values(d):
	d1={}
	num=[]
	let=[]

	for (k,v) in list(d.items()):
		if v not in num and k not in let:
			d1[v]=k
			num.append(v)
			let.append(k)
	return (d1)
