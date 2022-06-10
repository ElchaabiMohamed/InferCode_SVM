import sys

# d = { "0" : "zero",
# 			"1" : "one", 
# 			"2" : "two", 
# 			"3" : "three", 
# 			"4" : "four", 
# 			"5" : "five",
# 			"6" : "six",
# 			"7" : "seven",
# 			"8" : "eight",
# 			"9" : "nine",
# 			"10" : "ten",}

def swap_keys_values(d):
	keys = []
	values = []
	newd = {}
	for word in d:
		keys.append(word)
	for word in d:
		values.append(d[word])
	for i in range(0, len(values)):
		newd[values[i]] = keys[i]
	sort = sorted(list(newd.items()), key = lambda x:x[1] )
	print(sort)
