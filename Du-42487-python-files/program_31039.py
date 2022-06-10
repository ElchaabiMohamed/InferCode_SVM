def swap_keys_values(d):
	dic={}
	values=[]
	notunique=[]
	for key in d:
		if d[key] in values:
			notunique.append(d[key])
		else:
			values.append(d[key])

	for key in d:
		if not d[key] in notunique:
			dic[d[key]]=key
	return dic



if __name__ == '__main__':
	main()