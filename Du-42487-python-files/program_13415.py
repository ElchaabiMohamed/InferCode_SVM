def swap_key_values(dick):
	newDick = {}
	for item in dick:
		newDick[dick[item]] = item
	return newDick