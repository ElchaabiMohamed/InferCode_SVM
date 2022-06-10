import sys

def swap_unique_keys_values(d):
	c = {}
	e = {}
	r = {}
	seen = {}
	for value in list(d.values()):
		if value not in c:
			c[value] = 1
		else:
			c[value] = c[value] + 1

	for (keys, values) in list(c.items()):
		if values == 2:
			e.append(keys)
			del values

	for key in e:
		for value in list(d.items()):
			if key not in value:
				r[value[0]] = value[1]

	my_dict = r
	new_dict = {v:k for (k, v) in list(my_dict.items())}
	return(new_dict)

def main():
	new_dict = swap_unique_keys_values(d = {"a" : 4, "b" : 7, "c" : 10, "d" : 7,})
	print((list(new_dict.items())))

if __name__ == "__main__":
	main()