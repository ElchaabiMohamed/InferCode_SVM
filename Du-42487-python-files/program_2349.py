import sys

def minimum(list):
	if len(list) == 1:
		return list[0]
	max_value = max(list)
	return 	list.remove(max_value)
