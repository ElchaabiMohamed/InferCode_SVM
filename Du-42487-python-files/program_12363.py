def swap_keys_values(dick):
	newDick = {}
	for item in dick:
		newDick[dick[item]] = item
	return newDick