def reverse_list(li):
	try:
		newli = []
		if len(li) == 1:
			return li
		x = li.pop(0)
		newli = reverse_list(li)
		newli.append(x)
		return newli
	except:
		return li