
my_dict = {"a" : 4, "b" : 7, "c" : 10}

def swap_keys_values(my_dict):
	new_dict = {}
	seen = []
	seen2 = []
	for k, v in list(my_dict.items()):
		if (v) not in seen:
			seen.append(v)
		if (v) in seen:
			seen2.append(v)
	new_dict = {v : k for (k,v) in list(my_dict.items()) if v not in seen2}
	return new_dict


def main():
	new_dict = swap(my_dict)
	for (k, v) in list(new_dict.items()):
		print((list(new_dict.items())))

if __name__ == '__main__':
	main()