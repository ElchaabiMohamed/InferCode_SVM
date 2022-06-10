def swap_unique_keys_values(dick):
	newDick = {}
	deleted = []
	for item in dick:
		if dick[item] not in newDick:
			newDick[dick[item]] = item
		else:
			deleted.append(dick[item])
	for item in deleted:
		del newDick[item]